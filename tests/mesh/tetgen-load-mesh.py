'''
Test TetGen load mesh interface.

Not sure what use it is to load a mesh.
'''
import sv
import vtk
import graphics as gr

## Create a TetGen mesher.
#
mesher = sv.meshing.create_mesher(sv.meshing.Kernel.TETGEN)

## Load a mesh. 
#
file_name = 'cylinder-mesh.vtu'
mesher.load_mesh(file_name)

## Generate surface mesh.
options = mesher.create_options(global_edge_size=0.75, surface_mesh_flag=True, volume_mesh_flag=False, mesh_wall_first=True)

## Set mesher options.
mesher.set_options(options)

## Set the face IDs for model walls.
face_ids = [1]
#mesher.set_walls(face_ids)

## Compute model boundary faces.
#mesher.compute_model_boundary_faces(angle=60.0)

## Generate the mesh. 
print("Generate mesh ...")
#mesher.generate_mesh()



## Show the mesh.
#
show_mesh = True
if show_mesh:
    win_width = 500
    win_height = 500
    renderer, renderer_window = gr.init_graphics(win_width, win_height)

    mesh = mesher.get_mesh()
    mesh_polydata = gr.convert_ug_to_polydata(mesh)
    gr.add_geom(renderer, mesh_polydata, color=[1.0, 1.0, 1.0], wire=True, edges=True)

    gr.display(renderer_window)


