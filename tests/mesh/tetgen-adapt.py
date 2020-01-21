'''
Test TetGen adapt interface.

Note: this currently does not work.
'''
import sv
import vtk
import graphics as gr

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
options = mesher.create_options(global_edge_size=0.75, surface_mesh_flag=True, volume_mesh_flag=True, mesh_wall_first=True)

# Set local edge size on a face.
options.local_edge_size = {'face_id':2, 'edge_size':0.2}

#print("options values: ")
#[ print("  {0:s}:{1:s}".format(key,str(value))) for (key, value) in sorted(options.get_values().items()) ]
#help(options)

## Load solid model into the mesher.
#  Note: must load solid before setting certain options!
#
file_name = 'cylinder.vtp'
mesher.load_model(file_name)

## Set mesher options.
mesher.set_options(options)

## Set the face IDs for model walls.
face_ids = ['a']
face_ids = 1
face_ids = []
face_ids = [1]
mesher.set_walls(face_ids)


## Compute model boundary faces.
mesher.compute_model_boundary_faces(angle=60.0)
face_info = mesher.get_model_face_info()
print("Mesh face info: " + face_info);

## Generate the mesh. 
mesher.generate_mesh()

## Get the mesh as a vtkUnstructuredGrid. 
mesh = mesher.get_mesh()
print("Mesh:");
print("  Number of nodes: {0:d}".format(mesh.GetNumberOfPoints()))
print("  Number of elements: {0:d}".format(mesh.GetNumberOfCells()))

## Mesh adapt? does not work.
#mesher.adapt()
#mesh = mesher.get_mesh()
#print("Mesh:");
#print("  Number of nodes: {0:d}".format(mesh.GetNumberOfPoints()))
#print("  Number of elements: {0:d}".format(mesh.GetNumberOfCells()))

