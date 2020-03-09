'''
Test MeshSim interface.
'''
import sv
import vtk
import graphics as gr

print(dir(sv.meshing))
print("Mesh generation kernel names: {0:s}".format(str(sv.meshing.Kernel.names)))

## Create a MeshSim mesher.
#
mesher = sv.meshing.create_mesher(sv.meshing.Kernel.MESHSIM)
print("Mesher: " + str(mesher))
mesher.set_solid_modeler_kernel(sv.solid.Kernel.PARASOLID)

## Load the aorta iliac model.
#
# face id="1647" name="wall_right_iliac" type="wall" 
# face id="1638" name="right_iliac" type="cap" 
# face id="1692" name="wall_aorta" type="wall" 
# face id="1685" name="aorta" type="cap" 
# face id="1683" name="aorta_2" type="cap" 
#
mesher.load_model("aorta-iliac.xmt_txt")

## Mesh face info:  
#
#  {101 13 {wall_right_iliac}}  
#  {76 7 {right_iliac}}  
#  {73 63 {wall_aorta}}  
#  {96 57 {aorta}}  
#  {98 60 {aorta_2}} 
#
#  face ids: 13, 7, 63, 57, 60
#
face_info = mesher.get_model_face_info()
print("Mesh face info: " + face_info)

## Set meshing options.
#
print("Set meshing options ... ")
options = mesher.create_options(global_edge_size={'edge_size':0.5, 'absolute':True}, surface_mesh_flag=True, volume_mesh_flag=True)

# Set local edge size on a face.
#options.local_edge_size = [ {'face_id':13, 'edge_size':0.2, 'absolute':True} ]

# Print options.
print("options values: ")
[ print("  {0:s}:{1:s}".format(key,str(value))) for (key, value) in sorted(options.get_values().items()) ]

# Set mesher options.
mesher.set_options(options)

## Generate the mesh. 
mesher.generate_mesh()

#mesher.write_mesh(file_name='aorta-iliac-mesh.vtu')

## Show the mesh.
#
show_mesh = True
if show_mesh:
    win_width = 500
    win_height = 500
    renderer, renderer_window = gr.init_graphics(win_width, win_height)

    #mesh_polydata = gr.convert_ug_to_polydata(mesh)
    mesh_surface = mesher.get_surface()
    #gr.add_geom(renderer, mesh_surface, color=[1.0, 1.0, 1.0], wire=True, edges=True)
    gr.add_geom(renderer, mesh_surface, color=[1.0, 1.0, 1.0], wire=False, edges=True)

    #mesh_model_polydata = mesher.get_model_polydata()
    #gr.add_geom(renderer, mesh_model_polydata, color=[0.0, 1.0, 1.0], wire=True, edges=True)

    #face1_polydata = mesher.get_face_polydata(1)
    #gr.add_geom(renderer, face1_polydata, color=[1.0, 0.0, 0.0], wire=False, edges=True)

    #face2_polydata = mesher.get_face_polydata(2)
    #gr.add_geom(renderer, face2_polydata, color=[0.0, 1.0, 0.0], wire=False, edges=True)

    #face3_polydata = mesher.get_face_polydata(3)
    #gr.add_geom(renderer, face3_polydata, color=[0.0, 0.0, 1.0], wire=False, edges=True)

    gr.display(renderer_window)



