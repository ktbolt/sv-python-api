'''
Test setting MeshSim options using MeshSimOptions Python class.
'''
import sv

#print("dir(sv.meshing): ")
#print(dir(sv.meshing))

# Create options object.
global_edge_size = { 'edge_size':0.1, 'absolute':True }
options = sv.meshing.pMeshSimOptions(global_edge_size=global_edge_size, surface_mesh_flag=True, volume_mesh_flag=True)

#print("dir(options): ")
#print(dir(options))

#print("dir(local edge size): ")
#print(dir(options.local_edge_size))

#------------------
# global_edge_size 
#------------------
if False:
    print(" ")
    print("Set global edge size ... ")
    options.global_edge_size = {'edge_size':4.0, 'absolute':True } 
    print("Global edge size: " + str(options.global_edge_size))
    #
    # Test error conditions.
    #options.global_edge_size = {'edge_size':1, 'absolute':True } 
    #options.global_edge_size = {'edge_size':'a', 'absolute':True } 

#-----------------
# local_edge_size 
#-----------------
if False:
    print("Set local edge size ... ")
    options.local_edge_size =  [ {'face_id':1, 'edge_size':1.0, 'absolute':True } ]
    options.local_edge_size.append( {'face_id':2, 'edge_size':2.0, 'absolute':True } ) 
    # Test error conditions.
    options.local_edge_size.append( {'face_id':2, 'edge_siz':2.0, 'absolute':True } ) 

#-------------------
# surface_mesh_flag
#-------------------
if False:
    options.surface_mesh_flag = True 
    # Test error conditions.
    #options.surface_mesh_flag = 1 

#---------------
# print options 
#---------------
print("----------")
print("Options ... ")
options.print()

