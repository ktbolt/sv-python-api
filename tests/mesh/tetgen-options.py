'''
Test TetGen interface.
'''
import sv
import vtk

## Create a TetGen mesher.
mesher = sv.meshing.create_mesher(sv.meshing.Kernel.TETGEN)
mesher.set_solid_modeler_kernel(sv.solid.Kernel.POLYDATA)

## Set meshing options.
#
print("Set meshing options ... ")
#options = mesher.create_options(global_edge_size=0.1, surface_mesh_flag=True, volume_mesh_flag=True, mesh_wall_first=True)
#options = mesher.create_options(global_edge_size=0.1, surface_mesh_flag=True, volume_mesh_flag=True, mesh_wall_first=False)
#options = mesher.create_options(global_edge_size=0.1, surface_mesh_flag=1, volume_mesh_flag=True, mesh_wall_first=True)

#options = mesher.create_options(global_edge_size=0.1, surface_mesh_flag=True, volume_mesh_flag=True)

options = sv.meshing.TetGenOptions(global_edge_size=0.1, surface_mesh_flag=True, volume_mesh_flag=True)

#------------------ 
# global_edge_size
#------------------ 
#
#options.global_edge_size = "a"
#options.global_edge_size = 0.5
#options.epsilon = 0.5
#print("options.global_edge_size: " + str(options.global_edge_size))
#print("options.local_edge_size: " + str(options.local_edge_size))

#----------
# add_hole
#----------
#
#options.add_hole = 1.0
#options.add_hole = ["a", 2.0, 3.0]
#options.add_hole = [1.0, 2.0]
#options.add_hole = [1.0, 2.0, 3.0]
#print("options.add_hole: " + str(options.add_hole))

#-------------------
# surface_mesh_flag
#-------------------
#
#options.surface_mesh_flag = False
#print("options.surface_mesh_flag: " + str(options.surface_mesh_flag))

#---------------
# add_subdomain
#---------------
#
#options.add_subdomain = {'coordinate':[1.0,2.0,3.0], 'region_size':10}
#options.add_subdomain = {'coordinate':3.0, 'region_size':10}
#options.add_subdomain = {'coordinate':[1.0,2.0,3.0], 'region_size':'a'}

#add_subdomain_param = options.create_add_subdomain_parameter(coordinate=[1,2,3], region_size=10)
#add_subdomain_param = options.create_add_subdomain_parameter(coordinate=[1,2,'a'], region_size=10)
#print("add_subdomain_param: " + str(add_subdomain_param))

#options.add_subdomain = add_subdomain_param 
#print("options.add_subdomain: " + str(options.add_subdomain))

#options.quiet = True 
#print("options.quiet: " + str(options.quiet))

#-----------------
# Local edge size 
#-----------------
# options.local_edge_size is a list of {'face_id': int, 'edge_size': float}.
#
#local_edge_size = options.create_local_edge_size_parameter(face_id=1, edge_size=0.1)
#options.local_edge_size = local_edge_size
#options.local_edge_size = {'face_id': 'a', 'edge_size': 0.1}
#options.local_edge_size = {'face_id': 1, 'edge_size': 0.1}
#options.add_local_edge_size_parameter(face_id=2, edge_size=0.2)

#-------------------
# print all options
#-------------------
#
print("Options values: ")
[ print("  {0:s}:{1:s}".format(key,str(value))) for (key, value) in sorted(options.get_values().items()) ]
#help(options)

#--------------------
# Set mesher options
#--------------------
#
#mesher.set_options(options)


