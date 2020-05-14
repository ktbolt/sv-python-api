'''
Test modeling.Modeler methods. 
'''
import sv
import vtk

print(dir(sv))

def display(renderer_win):
    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
    interactor.SetRenderWindow(renderer_win)
    interactor.Start()

def add_geom(renderer, polydata, color=[1.0, 1.0, 1.0], wire=False, opacity=1.0):
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(polydata)
    mapper.SetScalarVisibility(False)
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(color[0], color[1], color[2])
    actor.GetProperty().SetPointSize(5)
    actor.GetProperty().SetOpacity(opacity)
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
#print(dir(sv.modeling))
#print("Solid modeling kernel names: {0:s}".format(str(sv.modeling.Kernel.names)))

# Get the modeling.Model methods.
modeler_methods = [m for m in dir(sv.modeling.Modeler) if ('__' not in m)]
print("modeling.Modeler methods: {0:s}".format(str(modeler_methods)))

# Create a modeler.
kernel = sv.modeling.Kernel.OPENCASCADE
kernel = sv.modeling.Kernel.POLYDATA
modeler = sv.modeling.Modeler(kernel)

#----------------------------------------------------
# cylinder
#----------------------------------------------------
print("Create a cylinder ...") 
center = [0.0, 0.0, 0.0]
axis = [0.0, 0.0, 1.0]
radius = 1.5
length = 10.0
cylinder = modeler.cylinder(radius, length, center, axis)
print("cylinder type: " + str(type(cylinder)))
cylinder_polydata = cylinder.get_polydata() 
print("Cylinder: num nodes: {0:d}".format(cylinder_polydata.GetNumberOfPoints()))

center = [0.0, 0.0, 2.0]
axis = [1.0, 0.0, 0.0]
radius = 0.5
length = 10.0
cylinder1 = modeler.cylinder(radius, length, center, axis)
print("cylinder type: " + str(type(cylinder)))
cylinder1_polydata = cylinder1.get_polydata()


#----------------------------------------------------
# union 
#----------------------------------------------------
print("Union two cylinders ...")
union_result = modeler.union(model1=cylinder, model2=cylinder1)
union_result_polydata = union_result.get_polydata()
union_result.write(file_name="cyl_cyl_union", format="vtp")

renderer, renderer_win = init_graphics()
#add_geom(renderer, cylinder_polydata, color=[1.0,0.0,0.0], wire=True)
#add_geom(renderer, cylinder1_polydata, color=[0.0,1.0,0.0], wire=True)
add_geom(renderer, union_result_polydata, color=[0.0,1.0,0.0], wire=True)

#add_geom(renderer, box_polydata, color=[0.0,1.0,0.0], wire=True)
#add_geom(renderer, subtract_result_polydata, opacity=0.5)
display(renderer_win)

