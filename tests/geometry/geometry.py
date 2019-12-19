import sv
import vtk

#print(dir(sv))
print(dir(sv.geometry))

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
        actor.GetProperty().SetLineWidth(1.0)
    renderer.AddActor(actor)

def init_graphics():
    '''
    Create renderer and graphics window.
    '''
    renderer = vtk.vtkRenderer()
    renderer_win = vtk.vtkRenderWindow()
    renderer_win.AddRenderer(renderer)
    renderer.SetBackground(0.8, 0.8, 0.8)
    renderer_win.SetSize(500, 500)
    renderer_win.Render()
    renderer_win.SetWindowName("Vis Modeler")
    return renderer, renderer_win


## Create a modeler.
#
kernel = sv.solid.Kernel.POLYDATA
modeler = sv.solid.Modeler(kernel)
renderer, renderer_window = init_graphics()

## Create a cylinder.
#
print("Create a cylinder.")
center = [0.0, 0.0, 0.0]
axis = [0.0, 0.0, 1.0]
radius = 1.5
length = 10.0
cylinder = modeler.cylinder(radius, length, center, axis)
cylinder_polydata = cylinder.get_polydata()

#------------------------------ 
# classify
#------------------------------ 
point = [0.0, 0.0, 0.0]
result = sv.geometry.classify(cylinder_polydata, point)
print("Classify point result: " + str(result))
sphere = vtk.vtkSphereSource()
sphere.SetCenter(point[0], point[1], point[2])
sphere.SetRadius(0.2)
sphere.Update()
sphere_pd = sphere.GetOutput()
add_geom(renderer, sphere_pd, color=[1.0, 1.0, 1.0])

## Show geometry.
#
add_geom(renderer, cylinder_polydata, color=[1.0,0.0,0.0], wire=True)
display(renderer_window)

