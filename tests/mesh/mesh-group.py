'''
This scipt tests reading in an SV Mesh from an .msh file.
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
    renderer_win.SetWindowName("Vis Meshing")
    return renderer, renderer_win

## Read an SV mesh group file. 
#
home = str(Path.home())
mesh_name = "demo.msh"
mesh_name = "demo-test.msh"
file_name = home + "/SimVascular/DemoProject/Meshes/" + mesh_name
print("Read SV msh file: {0:s}".format(file_name))
demo_meshes = sv.meshing.Group(file_name)
#num_meshes = demo_models.number_of_models()
#print("Number of models: {0:d}".format(num_models))

# Get a mesh for time 0.
mesher, options = demo_meshes.get_mesh(0)
print("Mesher type: " + str(type(mesher)))
print("Options type: " + str(type(options)))
options.mesh_wall_first = True
print("Options ... ")
values = options.get_values()
for k,v in values.items():
    print("  {0:s}: {1:s}".format(k,str(v)))
face_info = mesher.get_model_face_info()
print("Mesh face info: " + face_info)

## Set the face IDs for model walls.
#face_ids = [1, 2]
#mesher.set_walls(face_ids)

## Set mesher options.
mesher.set_options(options)

## Generate the mesh. 
mesher.generate_mesh()

## Write the mesh.
mesher.write_mesh(file_name=mesh_name+'.vtu')

#mesh_surface = mesher.get_surface()
#print("Number of surface mesh nodes: {0:d}".format(mesh_surface.GetNumberOfPoints()))

#mesh_model_polydata = mesher.get_model_polydata()
#print("Number of volume mesh nodes: {0:d}".format(mesh_model_polydata.GetNumberOfPoints()))

#face1_polydata = mesher.get_face_polydata(1)
#print("Face 1 number of nodes: {0:d}".format(face1_polydata.GetNumberOfPoints()))
#gr.add_geom(renderer, face1_polydata, color=[1.0, 0.0, 0.0], wire=False, edges=True)

#display(renderer_win)

