'''
Test solid.Modeler methods. 
'''
import sv
import vtk

print(dir(sv))

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

# Get the solid.Model methods.
modeler_methods = [m for m in dir(sv.solid.Modeler) if ('__' not in m)]
print("solid.Modeler methods: {0:s}".format(str(modeler_methods)))

# Create a modeler.
kernel = sv.solid.Kernel.OPENCASCADE
kernel = sv.solid.Kernel.POLYDATA
modeler = sv.solid.Modeler(kernel)

#----------------------------------------------------
# box
#----------------------------------------------------
print("Create a box ...")
center = [0.0, 0.0, 0.0]
box = modeler.box(center, length=6.0, height=6.0, width=6.0)
print("box type: " + str(type(box)))
box_polydata = box.get_polydata()
print("Box: num nodes: {0:d}".format(box_polydata.GetNumberOfPoints()))

#----------------------------------------------------
# cylinder
#----------------------------------------------------
print("Create a cylinder ...") 
center = [0.0, 0.0, 0.0]
axis = [0.0, 0.0, 1.0]
radius = 1.5
length = 10.0
length = 3.0
cylinder = modeler.cylinder(radius, length, center, axis)
print("cylinder type: " + str(type(cylinder)))
cylinder_polydata = cylinder.get_polydata() 
print("Cylinder: num nodes: {0:d}".format(cylinder_polydata.GetNumberOfPoints()))

#----------------------------------------------------
# ellipsoid 
#----------------------------------------------------
# [TODO:DaveP] The cvSolidModel MakeEllipsoid method is not implemented.
'''
print("Create an ellipsoid ...")
center = [0.0, 0.0, 0.0]
radii = [1.0, 2.0, 3.0]
ellipsoid = modeler.ellipsoid(radii, center)
print("ellipsoid type: " + str(type(ellipsoid)))
ellipsoid_polydata = ellipsoid.get_polydata()
print("Ellipsoid: num nodes: {0:d}".format(ellipsoid_polydata.GetNumberOfPoints()))
'''

#----------------------------------------------------
# intersect 
#----------------------------------------------------
print("Intersect box and cylinder ...")
intersect_result = modeler.intersect(box, cylinder)
print("intersect_result type: " + str(type(intersect_result)))
intersect_result_polydata = intersect_result.get_polydata()
print("Intersect esult: num nodes: {0:d}".format(intersect_result_polydata.GetNumberOfPoints()))
'''
renderer, renderer_win = init_graphics()
add_geom(renderer, cylinder_polydata, color=[1.0,0.0,0.0], wire=True)
add_geom(renderer, box_polydata, color=[0.0,1.0,0.0], wire=True)
add_geom(renderer, intersect_result_polydata)
display(renderer_win)
'''

#----------------------------------------------------
# read 
#----------------------------------------------------
print("Read solid model file ...")
file_name = "cylinder.stl"
solid_model = modeler.read(file_name)

#----------------------------------------------------
# sphere 
#----------------------------------------------------
print("Create an sphere ...")
center = [0.0, 0.0, 0.0]
radius = 1.0
sphere = modeler.sphere(radius, center)
print("sphere type: " + str(type(sphere)))
sphere_polydata = sphere.get_polydata()
print("Sphere: num nodes: {0:d}".format(sphere_polydata.GetNumberOfPoints()))

#----------------------------------------------------
# subtract 
#----------------------------------------------------
print("Subtract cylinder from box ...")
subtract_result = modeler.subtract(main=box, subtract=cylinder)
print("subtract_result type: " + str(type(subtract_result)))
subtract_result_polydata = subtract_result.get_polydata()
print("Subtract result: num nodes: {0:d}".format(subtract_result_polydata.GetNumberOfPoints()))
#subtract_result.write(file_name="box-minus-cylinder", format="vtp")
subtract_result.write(file_name="box-minus-cylinder-inside", format="vtp")

'''
renderer, renderer_win = init_graphics()
add_geom(renderer, cylinder_polydata, color=[1.0,0.0,0.0], wire=True)
add_geom(renderer, box_polydata, color=[0.0,1.0,0.0], wire=True)
add_geom(renderer, subtract_result_polydata)
display(renderer_win)
'''

#----------------------------------------------------
# union 
#----------------------------------------------------
print("Union box and cylinder ...")
union_result = modeler.union(box, cylinder)
print("union_result type: " + str(type(union_result)))
union_result_polydata = union_result.get_polydata() 
print("Union result: num nodes: {0:d}".format(union_result_polydata.GetNumberOfPoints()))
'''
renderer, renderer_win = init_graphics()
add_geom(renderer, cylinder_polydata, color=[1.0,0.0,0.0], wire=True)
add_geom(renderer, box_polydata, color=[0.0,1.0,0.0], wire=True)
add_geom(renderer, union_result_polydata)
display(renderer_win)
'''

