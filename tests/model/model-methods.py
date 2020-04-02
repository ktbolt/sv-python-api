'''
Test solid.Model methods. 
'''
import sv
import sys
import vtk

def display(renderer_win):
    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
    interactor.SetRenderWindow(renderer_win)
    interactor.Start()

def add_geom(renderer, polydata, color=[1.0, 1.0, 1.0], wire=False):
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(polydata)
    mapper.SetScalarVisibility(False)
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(color[0], color[1], color[2])
    actor.GetProperty().SetPointSize(5)
    if wire:
        actor.GetProperty().SetRepresentationToWireframe()
        actor.GetProperty().SetLineWidth(3.0)
    renderer.AddActor(actor)

def init_graphics():
    ## Create renderer and graphics window.
    #
    renderer = vtk.vtkRenderer()
    renderer_win = vtk.vtkRenderWindow()
    renderer_win.AddRenderer(renderer)
    renderer.SetBackground(0.8, 0.8, 0.8)
    renderer_win.SetSize(500, 500)
    renderer_win.Render()
    renderer_win.SetWindowName("Vis Modeler")
    return renderer, renderer_win


#print(dir(sv))
#print(dir(sv.solid))
#print("Solid modeling kernel names: {0:s}".format(str(sv.solid.Kernel.names)))

print("============= Test solid.Model methods ==========")

# Get the solid.Model methods.
model_methods = [m for m in dir(sv.solid.Model) if ('__' not in m)]
print("solid.Model methods: {0:s}".format(str(model_methods)))

## Create a modeler.
#
kernel = sv.solid.Kernel.OPENCASCADE 
kernel = sv.solid.Kernel.PARASOLID 
kernel = sv.solid.Kernel.POLYDATA
#
if not sv.solid.modeler_exists(kernel):
    print("No solid modeler for kernel: {0:s}".format(kernel))
    sys.exit(1)
#
modeler = sv.solid.Modeler(kernel)


## Create a cylinder.
center = [0.0, 0.0, 0.0]
axis = [0.0, 0.0, 1.0]
radius = 1.5
length = 10.0
cylinder = modeler.cylinder(radius, length, center, axis)
print("cylinder type: " + str(type(cylinder)))
'''
renderer, renderer_win = init_graphics()
cylinder_polydata = cylinder.get_polydata() 
add_geom(renderer, cylinder_polydata, color=[1.0,0.0,0.0], wire=False)
display(renderer_win)
'''

#----------------------------------------------------
# get_polydata 

#----------------------------------------------------
# apply4x4 
#----------------------------------------------------
# [TODO:DaveP] The C++ cvSolidModel Apply4x4() method is not implemented.
 
matrix = [ [1.0, 0.0, 0.0, 0.0 ], 
           [0.0, 1.0, 0.0, 0.0 ], 
           [0.0, 0.0, 1.0, 0.0 ], 
           [0.0, 0.0, 0.0, 1.0 ] ] 

# cylinder.apply4x4(matrix)

#----------------------------------------------------
# calculate_boundary_faces 
#----------------------------------------------------
angle = 60.0
#cylinder.calculate_boundary_faces(angle) 

#----------------------------------------------------
# check 
#----------------------------------------------------
# [TODO:DaveP] The C++ cvSolidModel check() method is not implemented.
#check_error = cylinder.check() 
#print("check_error: {0:d}".format(check_error))

#----------------------------------------------------
# classify_point 
#----------------------------------------------------
# [TODO:DaveP] The C++ cvSolidModel ClassifyPt() method is not implemented.
x = 0.0
y = 0.0
z = 0.0
#classify_result = cylinder.classify_point(x, y, z) 
#print("classify_result: {0:d}".format(classify_result))

#----------------------------------------------------
# delete_faces
#----------------------------------------------------
'''
print("---------- delete_faces ----------")
if kernel == sv.solid.Kernel.POLYDATA:
    angle = 90.0
    cylinder.calculate_boundary_faces(angle) 
face_ids = cylinder.get_face_ids()
print("Cylinder: Face IDs: {0:s}".format(str(face_ids)))
#
face_list = [ face_ids[0] ]
print("Cylinder: Delete face IDs: {0:s}".format(str(face_list)))
cylinder.delete_faces(face_list)
#cylinder.calculate_boundary_faces(angle) 
face_ids = cylinder.get_face_ids()
print("Cylinder: Face IDs after delete: {0:s}".format(str(face_ids)))
'''
#
'''
renderer, renderer_win = init_graphics()
cylinder_polydata = cylinder.get_polydata() 
add_geom(renderer, cylinder_polydata, color=[1.0,0.0,0.0], wire=False)
display(renderer_win)
'''

#----------------------------------------------------
# find_centroid 
#----------------------------------------------------
# [TODO:DaveP] The C++ cvSolidModel FindCentroid() method is not implemented.
#result = cylinder.find_centroid() 
#print("find_centroid: {0:s}".format(str(result)))

#----------------------------------------------------
# get_face_ids
#----------------------------------------------------
#face_ids = cylinder.get_face_ids()
#print("Cylinder: Face IDs: {0:s}".format(str(face_ids)))

#----------------------------------------------------
# get_face_normal
#----------------------------------------------------
# [TODO:DaveP] The C++ cvSolidModel GetFaceNormal() method is not implemented.
#face_normal = cylinder.get_face_normal(face_id=1, u=0.0, v=0.0)
#print("Cylinder: Face ID 1 normale: {0:s}".format(str(face_normal)))

#----------------------------------------------------
# get_face_polydata
#----------------------------------------------------
#face1_polydata = cylinder.get_face_polydata(face_id=1)
#face2_polydata = cylinder.get_face_polydata(face_id=2)
#face3_polydata = cylinder.get_face_polydata(face_id=3)
#print("Cylinder: Face 1 polydata num nodes: {0:d}".format(face1_polydata.GetNumberOfPoints()))
'''
renderer, renderer_win = init_graphics()
cylinder_polydata = cylinder.get_polydata() 
#add_geom(renderer, cylinder_polydata, color=[1.0,0.0,0.0], wire=True)
add_geom(renderer, face1_polydata, color=[1.0,0.0,0.0])
add_geom(renderer, face2_polydata, color=[1.0,1.0,0.0])
add_geom(renderer, face3_polydata, color=[1.0,0.0,1.0])
display(renderer_win)
'''
#----------------------------------------------------
# get_polydata 
#----------------------------------------------------
#cylinder_polydata = cylinder.get_polydata() 
#print("Cylinder: num nodes: {0:d}".format(cylinder_polydata.GetNumberOfPoints()))


#----------------------------------------------------
# write 
#----------------------------------------------------
# [TODO:DaveP] Format should be optional, with a default native format: 
#
#    Parasolid: xmt_txt
#    PolyData:  vtp
#
#
# For Parasolid.
#cylinder.write(file_name="cylinder") 
#
cylinder.write(file_name="cylinder", format="vtp") 
#cylinder.write(file_name="cylinder", format="brep") 
#
#print("Cylinder: num nodes: {0:d}".format(cylinder_polydata.GetNumberOfPoints()))


