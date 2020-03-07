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

## Set meshing options.
#
print("Set meshing options ... ")
options = mesher.create_options(global_edge_size=0.75, surface_mesh_flag=True, volume_mesh_flag=True)

# Set local edge size on a face.
options.local_edge_size = {'face_id':2, 'edge_size':0.2}




