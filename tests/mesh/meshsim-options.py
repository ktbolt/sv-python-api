'''
Test setting MeshSim options using MeshSimOptions Python class.
'''
import sv

# Create options object.
global_edge_size = { 'edge_size':0.1, 'absolute':True }
options = sv.meshing.pMeshSimOptions(global_edge_size=global_edge_size, surface_mesh_flag=True, volume_mesh_flag=True)

print("dir(options): ")
print(dir(options))

#print("dir(local edge size): ")
#print(dir(options.local_edge_size))

#-----------------
# local_edge_size 
#-----------------
print("Set local edge size ... ")
#options.local_edge_size =  [ {'face_id':1, 'edge_size':1.0, 'absolute':True } ]
#options.local_edge_size.append( {'face_id':2, 'edge_size':2.0, 'absolute':True } ) 

#-------------------
# surface_mesh_flag
#-------------------
options.surface_mesh_flag = True 

#---------------
# print options 
#---------------
print("----------")
print("Options ... ")
options.print()

