from pathlib import Path
import sv

#print(dir(sv))
#print(dir(sv.solid))

#
if not sv.solid.modeler_exists(sv.solid.Kernel.PARASOLID):
    print("No solid modeler for kernel: {0:s}".format(sv.solid.Kernel.PARASOLID))

## Read an SV model group file. 
#
home = str(Path.home())
file_name = home + "/SimVascular/DemoProject/Models/parasolid-model.mdl"
file_name = home + "/SimVascular/DemoProject/Models/demo.mdl"
file_name = home + "/SimVascular/DemoProject/Models/cascade-model.mdl"
print("Read SV mdl file: {0:s}".format(file_name))
demo_models = sv.solid.Group(file_name)
num_models = demo_models.number_of_models()
print("Number of models: {0:d}".format(num_models))

model = demo_models.get_model(0)
print("Model type: " + str(type(model)))
model_polydata = model.get_polydata() 
print("Model polydata: num nodes: {0:d}".format(model_polydata.GetNumberOfPoints()))


 

