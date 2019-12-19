'''
This scipt tests reading in an SV Model .mdl file.
'''
from pathlib import Path
import sv
import vtk

#print(dir(sv))
#print(dir(sv.solid))

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

## Check for existing modelers.
#
if not sv.solid.modeler_exists(sv.solid.Kernel.PARASOLID):
    print("No solid modeler for kernel: {0:s}".format(sv.solid.Kernel.PARASOLID))

if not sv.solid.modeler_exists(sv.solid.Kernel.OPENCASCADE):
    print("No solid modeler for kernel: {0:s}".format(sv.solid.Kernel.OPENCASCADE))

## Read an SV model group file. 
#
home = str(Path.home())
file_name = home + "/SimVascular/DemoProject/Models/cascade-model.mdl"
file_name = home + "/SimVascular/DemoProject/Models/parasolid-model.mdl"
file_name = home + "/SimVascular/DemoProject/Models/demo.mdl"
print("Read SV mdl file: {0:s}".format(file_name))
demo_models = sv.solid.Group(file_name)
num_models = demo_models.number_of_models()
print("Number of models: {0:d}".format(num_models))

model = demo_models.get_model(0)
print("Model type: " + str(type(model)))
face_ids = model.get_face_ids()
print("Model Face IDs: {0:s}".format(str(face_ids)))

model_polydata = model.get_polydata() 
print("Model polydata: num nodes: {0:d}".format(model_polydata.GetNumberOfPoints()))
print("Model polydata: num polygons: {0:d}".format(model_polydata.GetNumberOfCells()))

face1_polydata = model.get_face_polydata(face_id=1)
face2_polydata = model.get_face_polydata(face_id=2)
face3_polydata = model.get_face_polydata(face_id=3)
print("Model face 1 polydata: num nodes: {0:d}".format(face1_polydata.GetNumberOfPoints()))
print("Model face 2 polydata: num nodes: {0:d}".format(face2_polydata.GetNumberOfPoints()))

renderer, renderer_win = init_graphics()
#add_geom(renderer, model_polydata, color=[0.5,0.5,0.5], wire=True)
add_geom(renderer, face1_polydata, color=[1.0, 0.0, 0.0], wire=False)
add_geom(renderer, face2_polydata, color=[1.0, 1.0, 0.0], wire=False)
add_geom(renderer, face3_polydata, color=[1.0, 0.0, 1.0], wire=False)
display(renderer_win)

