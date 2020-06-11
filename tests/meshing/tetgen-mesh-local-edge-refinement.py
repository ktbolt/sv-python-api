'''
Test TetGen local edge (face) refinement. 
'''
from pathlib import Path
import sv
import sys
import vtk
sys.path.insert(1, '../graphics/')
import graphics as gr

## Create a TetGen mesher.
#
mesher = sv.meshing.create_mesher(sv.meshing.Kernel.TETGEN)

## Load solid model into the mesher.
#  Note: must load solid before setting certain options!
#
print("Read model ... ")
home = str(Path.home())
model_name = "demo"
file_name = home + "/SimVascular/DemoProject/Models/" + model_name + ".vtp"
mesher.load_model(file_name)

## Set the face IDs for model walls.
wall_face_ids = [1, 2]
mesher.set_walls(wall_face_ids)

## Compute model boundary faces.
# 
# If the model has faces already computed (i.e. has 'ModelFaceID' array) then
# don't call this, the face IDs will no longer match the original face IDs.
#
#mesher.compute_model_boundary_faces(angle=60.0)
face_ids = mesher.get_model_face_ids()
print("Mesh face info: " + str(face_ids))

## Set meshing options.
#
options = sv.meshing.TetGenOptions(global_edge_size=0.5, surface_mesh_flag=True, volume_mesh_flag=True, mesh_wall_first=True)
options.optimization = 3
options.quality_ratio = 1.4
options.use_mmg = True
options.no_bisect = True

## Set local edge sizes.
#
options.local_edge_size = [ {'face_id':1, 'edge_size':0.3} ]
options.local_edge_size_on = True 
#
# Error check.
#options.local_edge_size = [ {'bface_id':1, 'edge_size':0.3} ]
#options.local_edge_size = [ {'face_id':'a', 'edge_size':0.3} ]
#options.local_edge_size = [ 1, 0.3 ]

## Print options values
[ print("  {0:s}:{1:s}".format(key,str(value))) for (key, value) in sorted(options.get_values().items()) ]

## Generate the mesh. 
mesher.generate_mesh(options)

## Get the mesh as a vtkUnstructuredGrid. 
mesh = mesher.get_mesh()
print("Mesh:");
print("  Number of nodes: {0:d}".format(mesh.GetNumberOfPoints()))
print("  Number of elements: {0:d}".format(mesh.GetNumberOfCells()))

## Write the mesh.
mesher.write_mesh(file_name=model_name+'-local-edge-mesh.vtu')

## Show the mesh.
#
show_mesh = False
if show_mesh:
    win_width = 500
    win_height = 500
    renderer, renderer_window = gr.init_graphics(win_width, win_height)

    #mesh_polydata = gr.convert_ug_to_polydata(mesh)
    mesh_surface = mesher.get_surface()
    gr.add_geom(renderer, mesh_surface, color=[1.0, 1.0, 1.0], wire=True, edges=True)
    #gr.add_geom(renderer, mesh_polydata, color=[1.0, 1.0, 1.0], wire=False, edges=True)

    #mesh_model_polydata = mesher.get_model_polydata()
    #gr.add_geom(renderer, mesh_model_polydata, color=[0.0, 1.0, 1.0], wire=True, edges=True)

    face1_polydata = mesher.get_face_polydata(1)
    gr.add_geom(renderer, face1_polydata, color=[1.0, 0.0, 0.0], wire=False, edges=True)

    face2_polydata = mesher.get_face_polydata(2)
    gr.add_geom(renderer, face2_polydata, color=[0.0, 1.0, 0.0], wire=False, edges=True)

    face3_polydata = mesher.get_face_polydata(3)
    gr.add_geom(renderer, face3_polydata, color=[0.0, 0.0, 1.0], wire=False, edges=True)

    gr.display(renderer_window)

