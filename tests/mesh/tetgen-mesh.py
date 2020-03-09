'''
Test TetGen interface.
'''
import sv
import vtk
import graphics as gr

#print(dir(sv))
print(dir(sv.meshing))
print("Mesh generation kernel names: {0:s}".format(str(sv.meshing.Kernel.names)))

#mesher = sv.Mesher()
#print(str(mesher))

## Create a TetGen mesher.
#
mesher = sv.meshing.TetGen()
#mesher = sv.meshing.create_mesher(sv.meshing.Kernel.TETGEN)
print("Mesher: " + str(mesher))
mesher.set_solid_modeler_kernel(sv.solid.Kernel.POLYDATA)

## Set meshing options.
#
print("Set meshing options ... ")
options = mesher.create_options(global_edge_size=0.75, surface_mesh_flag=True, volume_mesh_flag=True, mesh_wall_first=True)

# Set local edge size on a face.
options.local_edge_size = {'face_id':2, 'edge_size':0.2}

#print("options values: ")
#[ print("  {0:s}:{1:s}".format(key,str(value))) for (key, value) in sorted(options.get_values().items()) ]
#help(options)

## Load solid model into the mesher.
#  Note: must load solid before setting certain options!
#
file_name = 'cylinder.vtp'
file_name = 'pd1.vtp'
mesher.load_model(file_name)

## Set mesher options.
mesher.set_options(options)

## Set the face IDs for model walls.
face_ids = ['a']
face_ids = 1
face_ids = []
face_ids = [1]
mesher.set_walls(face_ids)


## Compute model boundary faces.
mesher.compute_model_boundary_faces(angle=60.0)
face_info = mesher.get_model_face_info()
print("Mesh face info: " + face_info)

## Set boundary layer meshing options
#print("Set boundary layer meshing options ... ")
#mesher.set_boundary_layer_options(number_of_layers=4, constant_thickness=True, thickness_factor=0.8, layer_decreasing_ratio=0.8)

## Generate the mesh. 
mesher.generate_mesh()

## Get the mesh as a vtkUnstructuredGrid. 
mesh = mesher.get_mesh()
print("Mesh:");
print("  Number of nodes: {0:d}".format(mesh.GetNumberOfPoints()))
print("  Number of elements: {0:d}".format(mesh.GetNumberOfCells()))

## Write the mesh.
mesher.write_mesh(file_name='cylinder-mesh.vtu')

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



