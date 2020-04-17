'''
Test TetGen radius-based meshing.  
'''
from pathlib import Path
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

## Set meshing options.
#
print("Set meshing options ... ")
options = mesher.create_options(global_edge_size=0.2, surface_mesh_flag=True, volume_mesh_flag=True, mesh_wall_first=True)

## Load solid model into the mesher.
#  Note: must load solid before setting certain options!
#
print("Read model ... ")
home = str(Path.home())
model_name = "demo"
wall_face_ids = [1, 2]
file_name = home + "/SimVascular/DemoProject/Models/" + model_name + ".vtp"
mesher.load_model(file_name)

## Set mesher options.
print("Set mesh options ... ")
mesher.set_options(options)

## Set the face IDs for model walls.
mesher.set_walls(wall_face_ids)

## Compute model boundary faces.
mesher.compute_model_boundary_faces(angle=60.0)
face_info = mesher.get_model_face_info()
print("Mesh face info: " + face_info)

## Set sphere refinement meshing option.
print("Enable radius-based meshing ... ")
#mesher.enable_radius_based_meshing(edge_size=0.2)

radiusBasedMeshing = sv.meshing.TetGenRadiusBased(mesher)
#print("  radiusBasedMeshing: " + str(dir(radiusBasedMeshing)))
#radiusBasedMeshing.compute_centerlines()
#radiusBasedMeshing.compute_size_function(edge_size=0.2)
#radiusBasedMeshing.write_centerlines("demo-centerlines.vtp")
radiusBasedMeshing.load_centerlines("demo-centerlines.vtp")
mesher.enable_radius_based_meshing(radiusBasedMeshing)

if False:
    ## Generate the mesh. 
    mesher.generate_mesh()

    ## Get the mesh as a vtkUnstructuredGrid. 
    mesh = mesher.get_mesh()
    print("Mesh:");
    print("  Number of nodes: {0:d}".format(mesh.GetNumberOfPoints()))
    print("  Number of elements: {0:d}".format(mesh.GetNumberOfCells()))

