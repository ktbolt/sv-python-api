'''
Test setting MeshSim options using MeshSimOptions Python class.
'''
import sv

# Create options object.
options = sv.MeshSimOptions() 

#-----------------
# local_edge_size 
#-----------------
#
print("Set local edge size ... ")
options.local_edge_size.append( {'face_id':3, 'edge_size':3.0, 'absolute': True} )
options.local_edge_size.append( {'face_id':1, 'edge_size':1.0, 'absolute': True} )
#options.local_edge_size = [ {'face_id':1, 'edge_size':1.0}, {'face_id':2, 'edge_size':2.0} ]
#options.local_edge_size.clear()
print("Set local edge size len: " + str(len(options.local_edge_size)))

print("Create meshing options ... ")
global_edge_size = {'edge_size':0.1, 'absolute':True}
c_options = sv.meshing.MeshSimOptions(global_edge_size=global_edge_size, surface_mesh_flag=True, volume_mesh_flag=True)

c_options.check( options )

