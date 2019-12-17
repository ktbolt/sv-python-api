'''
Test solid.Modeler read method. 
'''
import sv
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

# Get the solid.Model methods.
modeler_methods = [m for m in dir(sv.solid.Modeler) if ('__' not in m)]
print("solid.Modeler methods: {0:s}".format(str(modeler_methods)))

# Create a modeler.
kernel = sv.solid.Kernel.POLYDATA
kernel = sv.solid.Kernel.PARASOLID
kernel = sv.solid.Kernel.OPENCASCADE
#
if not sv.solid.modeler_exists(kernel):
    print("No solid modeler for kernel: {0:s}".format(kernel))
    sys.exit(1)
#
modeler = sv.solid.Modeler(kernel)

#----------------------------------------------------
# read 
#----------------------------------------------------
print("Read solid model file ...")
file_name = "cylinder.stl"

if kernel == sv.solid.Kernel.OPENCASCADE:
    file_name = "cylinder.brep"
elif kernel == sv.solid.Kernel.PARASOLID:
    file_name = "cylinder.xmt_txt"

solid_model = modeler.read(file_name)
solid_model_polydata = solid_model.get_polydata()
print("Solid model type: " + str(type(solid_model)))
print("Solid model: num nodes: {0:d}".format(solid_model_polydata.GetNumberOfPoints()))

'''
renderer, renderer_win = init_graphics()
add_geom(renderer, solid_model_polydata, color=[1.0,0.0,0.0], wire=True)
display(renderer_win)
'''
