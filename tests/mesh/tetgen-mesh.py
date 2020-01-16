'''
Test TetGen interface.
'''
import sv
import vtk

#print(dir(sv))
print(dir(sv.meshing))
print("Mesh generation kernel names: {0:s}".format(str(sv.meshing.Kernel.names)))

#mesher = sv.Mesher()
#print(str(mesher))

## Create a TetGen mesher.
#
mesher = sv.meshing.create_mesher(sv.meshing.Kernel.TETGEN)
print("Mesher: " + str(mesher))
mesher.set_solid_modeler_kernel(sv.solid.Kernel.POLYDATA)
print(mesher.available())

## Set meshing options.
#
print("Set meshing options ... ")
options = mesher.create_options(global_edge_size=0.1, surface_mesh_flag=1, volume_mesh_flag=1, mesh_wall_first=1)
#options.global_edge_size = "a"
#options.global_edge_size = 0.5
options.epsilon = 0.5

print("options.global_edge_size: " + str(options.global_edge_size))

print("options values: ")
[ print("  {0:s}:{1:s}".format(key,str(value))) for (key, value) in sorted(options.get_values().items()) ]

#help(options)
mesher.set_options(options)

#file_name = 'cylinder.vtp'
#mesher.load_model(file_name)

