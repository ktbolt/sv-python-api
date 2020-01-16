'''
Test the sv.meshing TetGenOptions() class. 
'''
import sv

options = sv.meshing.TetGenOptions()
options.global_edge_size = -1.0

print("options.global_edge_size: " + str(options.global_edge_size))
print("options.surface_mesh_flag: " + str(options.surface_mesh_flag))

#help(options)


