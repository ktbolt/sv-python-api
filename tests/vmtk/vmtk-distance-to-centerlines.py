'''
Test vmtk.distance_to_centerlines() method.
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

# Read model geometry.
print("Read surface model file ...")
file_name = "aorta.vtp"
model = modeler.read(file_name)
model_polydata = model.get_polydata()
print("Model: num nodes: {0:d}".format(model_polydata.GetNumberOfPoints()))
gr.add_geom(renderer, model_polydata, color=[0.0, 1.0, 0.0], wire=False)

# Get model center.
com_filter = vtk.vtkCenterOfMass()
com_filter.SetInputData(model_polydata)
com_filter.SetUseScalarsAsWeights(False)
com_filter.Update()
center = com_filter.GetCenter()

## Print data arrays.
#
num_cells = model_polydata.GetNumberOfCells()
num_arrays = model_polydata.GetCellData().GetNumberOfArrays()
print("Model: num cell data arrays: {0:d}".format(num_arrays))
for i in range(num_arrays):
  data_type = model_polydata.GetCellData().GetArray(i).GetDataType()
  data_name = model_polydata.GetCellData().GetArrayName(i)
  cell_data = model_polydata.GetCellData().GetArray(data_name)
  print("Data name: {0:s}".format(data_name))
  if (data_name == "CapID") or (data_name == "ModelFaceID"):
      ids = set()
      for cell_id in range(num_cells):
          value = cell_data.GetValue(cell_id)
          ids.add(value)
      print("  Number of IDs: {0:d}".format(len(ids)))
      print("  IDs: {0:s}".format(str(ids)))

## Calculate centelines. 
# Use face IDs.
inlet_ids = [3]
outlet_ids = [5, 4]
centerlines_polydata = sv.vmtk.centerlines(model_polydata, inlet_ids, outlet_ids, use_face_ids=True)
gr.add_geom(renderer, centerlines_polydata, color=[1.0, 0.0, 0.0], wire=True, line_width=3.0)

## Calculate distance to centelines. 
#
# This returns a surface with 'DistanceToCenterlines' point data.
distance_centerlines_polydata = sv.vmtk.distance_to_centerlines(model_polydata, centerlines_polydata) 

print("Distance to centerlines: cell data arrays: ")
num_cell_arrays = distance_centerlines_polydata.GetCellData().GetNumberOfArrays()
for i in range(num_cell_arrays):
  data_name = distance_centerlines_polydata.GetCellData().GetArrayName(i)
  print("Data name: {0:s}".format(data_name))

print("Distance to centerlines: point data arrays: ")
num_point_arrays = distance_centerlines_polydata.GetPointData().GetNumberOfArrays()
for i in range(num_point_arrays):
  data_name = distance_centerlines_polydata.GetPointData().GetArrayName(i)
  print("Data name: {0:s}".format(data_name))

## Show geometry.
#
camera = renderer.GetActiveCamera();
#camera.Zoom(0.5)
#camera.SetPosition(center[0], center[1], center[2])
camera.SetFocalPoint(center[0], center[1], center[2])
data_name = "ModelFaceID"
gr.display(renderer, renderer_window, model_polydata, data_name)


