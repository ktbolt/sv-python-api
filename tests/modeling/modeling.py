import sv
import vtk

#print(dir(sv))
print(dir(sv.modeling))
print("Modeling kernel names: {0:s}".format(str(sv.modeling.Kernel.names)))

## Create a polydata modeler.
#
modeler = sv.modeling.Modeler(sv.modeling.Kernel.POLYDATA)

## Create a cylinder.
#
print("Create a cylinder ...") 
center = [0.0, 0.0, 0.0]
axis = [0.0, 0.0, 1.0]
radius = 0.25
length = 4.0
cyl = modeler.cylinder(radius, length, center, axis)
print("cyl type: " + str(type(cyl)))
cyl_polydata = cyl.get_polydata() 
print("Cylinder: num nodes: {0:d}".format(cyl_polydata.GetNumberOfPoints()))

## Create a box.
#
print("Create a box ...")
center = [0.0, 0.0, 0.0]
box = modeler.box(center, length=3.0, height=1.0, width=2.0)
#box = modeler.box3d(center)
#box = modeler.box3d(center, length=3.0)
#box = modeler.box3d(center, width, height, length)
print("box type: " + str(type(box)))
box_polydata = box.get_polydata()
print("Box: num nodes: {0:d}".format(box_polydata.GetNumberOfPoints()))

## Union cyl and box.
#
union_result = modeler.union(box, cyl)
union_result_polydata = union_result.get_polydata()
union_result.write(file_name="cylinder_box", format="vtp")

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
mapper.SetInputData(cyl_polydata)
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(1.0, 0.0, 0.0)
actor.GetProperty().SetPointSize(5)
actor.GetProperty().SetRepresentationToWireframe()
renderer.AddActor(actor)

# Add box polydata.
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(box_polydata)
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(0.0, 1.0, 0.0)
actor.GetProperty().SetPointSize(5)
actor.GetProperty().SetRepresentationToWireframe()
renderer.AddActor(actor)

# Add union polydata.
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(union_result_polydata)
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(0.0, 1.0, 0.0)
actor.GetProperty().SetPointSize(5)
#actor.GetProperty().SetRepresentationToWireframe()
renderer.AddActor(actor)

## Create a trackball interacter to transoform the geometry using the mouse.
#
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
interactor.SetRenderWindow(renderer_win)
interactor.Start()

