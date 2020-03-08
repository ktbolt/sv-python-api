'''
Test MeshSim options. 
'''
import sv
import vtk

## Create a MeshSim mesher.
'''
mesher = sv.meshing.create_mesher(sv.meshing.Kernel.MESHSIM)
mesher.set_solid_modeler_kernel(sv.solid.Kernel.PARASOLID)
mesher.load_model("m1.xmt_txt")
'''

## Set meshing options.
#
print("Set meshing options ... ")
global_edge_size = {'edge_size':0.1, 'absolute':True}
options = sv.meshing.MeshSimOptions(global_edge_size=global_edge_size, surface_mesh_flag=True, volume_mesh_flag=True)

#-------------------
# surface_mesh_flag
#-------------------
#
#options.surface_mesh_flag = False
#print("options.surface_mesh_flag: " + str(options.surface_mesh_flag))

#-----------------
# local_edge_size 
#-----------------
#
#local_edge_size = {'face_id':1, 'edge_size':1.0}
#options.local_edge_size = [ {'face_id':1, 'edge_size':1.0}, {'face_id':2, 'edge_size':2.0} ]
#options.local_edge_size.append( {'face_id':3, 'edge_size':3.0} )
#options.local_edge_size.clear()

# use set and add to build list.
options.set_local_edge_size(face_id=1, edge_size=1.0)
options.add_local_edge_size(face_id=2, edge_size=2.0)
print(str(options.add_local_edge_size))

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
# mesher.set_options(options)


