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
options = mesher.create_options()
#options.global_edge_size = "a"
print("options.global_edge_size: " + str(options.global_edge_size))

options_values = options.get_values() 
print("options values: " + str(options_values))

#help(options)
mesher.set_options(options)

#file_name = 'cylinder.vtp'
#mesher.load_model(file_name)

