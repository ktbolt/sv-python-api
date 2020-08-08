'''Generate html documentation.
'''
import sv
import inspect
from pprint import pprint

## Define some html tags.
#
FUNCTION_LEGEND = '<legend style="font-size:20px; text-align:left"> <b> Functions </b> </legend> \n'
METHOD_LEGEND = '<legend style="font-size:20px; text-align:left"> <b> Methods </b> </legend> \n'
DATA_LEGEND = '<legend style="font-size:20px; text-align:left"> <b> Data </b> </legend> \n'
BREAK = '<br>\n'
PARAGRAPH_START = '<pre class="PythonMethodsPre">'
PARAGRAPH_END = '</pre> \n'

def write_function_desc(fp, functions, show_header=True):
    '''Write html for functions.
    '''
    if len(functions) == 0:
        return
    if show_header:
        fp.write(FUNCTION_LEGEND)

    for name, data in functions:
        print(">>> function: {0:s} {1:s} ".format(name, str(data)))
        doc = "   " + data.__doc__
        fp.write(PARAGRAPH_START)
        fp.write("<strong>" + name + "</strong>")
        fp.write('\n')
        fp.write(doc)
        fp.write('\n')
        fp.write(PARAGRAPH_END)
        fp.write('\n')
        fp.write('\n')


def write_member_desc(fp, members):
    '''Write html for class member data.
    '''
    if len(members) == 0:
        return
    fp.write(DATA_LEGEND)

    for name, data in members: 
        print(">>> member: {0:s} {1:s} ".format(name, str(data)))
        doc = "   " + data.__doc__
        fp.write(PARAGRAPH_START)
        fp.write("<strong>" + name + "</strong>")
        fp.write('\n')
        fp.write(doc)
        fp.write('\n')
        fp.write(PARAGRAPH_END)
        fp.write('\n')
        fp.write('\n')

def write_methods_desc(fp, methods):
    '''Write html for class methods.
    '''
    if len(methods) == 0:
        return
    fp.write(METHOD_LEGEND)
    for name, data in methods: 
        print(">>> method: {0:s} {1:s} ".format(name, str(data)))
        doc = data.__doc__
        if doc == None:
            print("**** WARNING: No documentation found.")
            continue
        # Highlight the method name.
        func_desc = doc[:doc.find("(")]
        #func_desc = doc[:doc.find(")")+1]
        print("    func_desc: '{0:s}' ".format(func_desc))
        doc = doc.replace(func_desc, "<strong>" + func_desc + "</strong>", 1)
        #doc_list = doc.split("\n")
        #print(str(doc_list))
        #fp.write(''.join(doc_list))
        fp.write(PARAGRAPH_START)
        fp.write(doc)
        fp.write(PARAGRAPH_END)
        fp.write(BREAK)

def write_class_desc(fp, name, data):
    '''Write html for a class.
    '''
    if name == "Error":
        return
    print('================= class {0:s} {1:s} =========================='.format(name, str(data)))
    doc = inspect.getdoc(data)
    func_loc = doc.find(name+"(")
    # Highlight the method name.
    if func_loc != -1:
        func_desc = doc[:doc.find("(")]
        #func_desc = doc[:doc.find(")")+1]
        doc = doc.replace(func_desc, "<strong>" + func_desc + "</strong>", 1)
    else:
        func_desc = ""

    fp.write(PARAGRAPH_START)
    fp.write(doc)
    fp.write(PARAGRAPH_END)
    #fp.write('<br>\n')
    first_method = True
    first_data = True
    methods = []
    members = []

    for meth_name, meth_data in inspect.getmembers(data):
        if meth_name.startswith('__'):
           continue
        if ("<method" in str(meth_data)):
            methods.append( (meth_name, meth_data) )
        elif ("<member" in str(meth_data)):
            members.append( (meth_name, meth_data) )
    #_for meth_name, meth_data

    fp.write(BREAK)
    write_methods_desc(fp, methods)
    write_member_desc(fp, members)

def write_module_desc(fp, module):
    doc = inspect.getdoc(module)
    doc_list = doc.split("\n")
    #print(str(doc_list))
    fp.write(''.join(doc_list[2:]))

def write_module_doc(name, module):
    print('\n\n')
    print('=========================================== write_module_doc ===========================================')
    print(module.__doc__)
    print('\n')
    #write_module_desc(fp, module)

    ## Get class and data members.
    #
    for key, data in inspect.getmembers(module, inspect.isclass):
        #print('\n')
        #print('================= class {0:s} {1:s} =========================='.format(key, str(data)))
        #print(data.__doc__)
        file_name = name + "_" + key + ".html"
        fp = open(file_name, "w")
        write_class_desc(fp, key, data)

    ## Get functions.
    #
    function_list = []
    for key, data in inspect.getmembers(module, inspect.isroutine):
        print('\n')
        print('================= function {0:s} {1:s} =========================='.format(key, str(data)))
        function_list.append( (key, data) )

    file_name = name + "_" + "functions" + ".html"
    fp = open(file_name, "w")
    if name == "dmg":
        show_header = False
    else:
        show_header = True 

    write_function_desc(fp, function_list, show_header)

write_module_doc("dmg", sv.dmg)
'''
write_module_doc("meshing", sv.meshing)
write_module_doc("modeling", sv.modeling)
write_module_doc("pathplanning", sv.pathplanning)
write_module_doc("segmentation", sv.segmentation)
'''

