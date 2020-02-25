'''
Test mesh_utils.remesh() method.
'''
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
file_name = "cylinder.vtp"
cylinder_model = modeler.read(file_name)
cylinder_polydata = cylinder_model.get_polydata()
print("Cylinder model: num nodes: {0:d}".format(cylinder_polydata.GetNumberOfPoints()))
print("Cylinder model: num cells: {0:d}".format(cylinder_polydata.GetNumberOfCells()))
gr.add_geom(renderer, cylinder_polydata, color=[1.0, 0.0, 0.0], wire=False, edges=True)

# Remesh cylinder surface.
remesh_polydata = sv.mesh_utils.remesh(cylinder_polydata)
#remesh_polydata = sv.mesh_utils.remesh(cylinder_polydata, log_file="remesh.log")
print("Remeshed model: num nodes: {0:d}".format(remesh_polydata.GetNumberOfPoints()))
print("Remeshed model: num cells: {0:d}".format(remesh_polydata.GetNumberOfCells()))

# Get cylinder center.
com_filter = vtk.vtkCenterOfMass()
com_filter.SetInputData(cylinder_polydata)
com_filter.SetUseScalarsAsWeights(False)
com_filter.Update()
center = com_filter.GetCenter()

## Show geometry.
#
camera = renderer.GetActiveCamera();
#camera.Zoom(0.5)
#camera.SetPosition(center[0], center[1], center[2])
camera.SetFocalPoint(center[0], center[1], center[2])
gr.display(renderer_window)



