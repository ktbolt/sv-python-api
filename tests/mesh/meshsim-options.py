'''
Test MeshSim options. 
'''
import sv
import vtk

## Create a MeshSim mesher.
mesher = sv.meshing.create_mesher(sv.meshing.Kernel.MESHSIM)
mesher.set_solid_modeler_kernel(sv.solid.Kernel.PARASOLID)
mesher.load_model("m1.xmt_txt")

## Set meshing options.
#
print("Set meshing options ... ")
global_edge_size = {'absolute':0.1, 'relative':1.0}
options = sv.meshing.MeshSimOptions(global_edge_size=global_edge_size, surface_mesh_flag=True, volume_mesh_flag=True)

#-------------------
# surface_mesh_flag
#-------------------
#
#options.surface_mesh_flag = False
#print("options.surface_mesh_flag: " + str(options.surface_mesh_flag))

#-------------------
# print all options
#-------------------
#
print("options values: ")
[ print("  {0:s}:{1:s}".format(key,str(value))) for (key, value) in sorted(options.get_values().items()) ]
#help(options)

#--------------------
# Set mesher options
#--------------------
#
mesher.set_options(options)


