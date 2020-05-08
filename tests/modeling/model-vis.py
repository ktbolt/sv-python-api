import sv
import vtk

print("Solid modeling kernel names: {0:s}".format(str(sv.modeling.Kernel.names)))

## Create a modeler.
#
kernel = sv.modeling.Kernel.PARASOLID
kernel = sv.modeling.Kernel.POLYDATA 
modeler = sv.modeling.Modeler(kernel)

## Create a cylinder.
#
print("Create a cylinder.") 
center = [0.0, 0.0, 0.0]
axis = [0.0, 0.0, 1.0]
radius = 1.5
length = 10.0
cyl = modeler.cylinder(radius, length, center, axis)
polydata = cyl.get_polydata() 

## Create renderer and graphics window.
#
renderer = vtk.vtkRenderer()
renderer_win = vtk.vtkRenderWindow()
renderer_win.AddRenderer(renderer)
renderer.SetBackground(0.8, 0.8, 0.8)
renderer_win.SetSize(500, 500)
renderer_win.Render()
renderer_win.SetWindowName("Vis SV Solid Model")

# Add cylinder polydata.
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(polydata)
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(1.0, 0.0, 0.0)
actor.GetProperty().SetPointSize(5)
renderer.AddActor(actor)

## Create a trackball interacter to transoform the geometry using the mouse.
#
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
interactor.SetRenderWindow(renderer_win)
interactor.Start()

