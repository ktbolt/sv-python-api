import sv
import vtk
import graphics as gr

win_width = 500
win_height = 500
renderer, renderer_window = gr.init_graphics(win_width, win_height)

# Create a modeler.
kernel = sv.solid.Kernel.POLYDATA
modeler = sv.solid.Modeler(kernel)

# Read cylinder geometry.
print("Read surface model file ...")
file_name = "cylinder-surface.vtp"
cylinder_model = modeler.read(file_name)
cylinder_polydata = cylinder_model.get_polydata()
print("Cylinder model: num nodes: {0:d}".format(cylinder_polydata.GetNumberOfPoints()))

# Get cylinder center.
com_filter = vtk.vtkCenterOfMass()
com_filter.SetInputData(cylinder_polydata)
com_filter.SetUseScalarsAsWeights(False)
com_filter.Update()
center = com_filter.GetCenter()

## Cap the cylinder surface.
#
# fill_id=0, increment_id=True -> ids = 0, 1
# fill_id=0, increment_id=False -> ids = 0, 0
# no fill_id arg -> ids = 1, 2
#
capped_cylinder = sv.vmtk.cap_with_ids(surface=cylinder_polydata, fill_id=0, increment_id=True)
print("Capped cylinder model: num nodes: {0:d}".format(capped_cylinder.GetNumberOfPoints()))

# Add geometry to vtk renderer.
gr.add_geom(renderer, cylinder_polydata, color=[0.5, 0.0, 0.0], wire=True)
gr.add_geom(renderer, capped_cylinder, color=[0.0, 1.0, 0.0], wire=False)

## Show geometry.
#
camera = renderer.GetActiveCamera();
#camera.Zoom(0.5)
#camera.SetPosition(center[0], center[1], center[2])
camera.SetFocalPoint(center[0], center[1], center[2])
gr.display(renderer_window)



