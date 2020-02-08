'''
Test TetGen adaptive meshing interface.
'''
import sv
import vtk
import graphics as gr

#print(dir(sv))
print(dir(sv.meshing))
print("Mesh generation adaptive kernel names: {0:s}".format(str(sv.meshing.AdaptiveKernel.names)))

## Create a TetGen Adaptive mesher.
#
adaptive_mesher = sv.meshing.create_adaptive_mesher(sv.meshing.AdaptiveKernel.TETGEN)
print("Mesher: " + str(adaptive_mesher))
#mesher.set_solid_modeler_kernel(sv.solid.Kernel.POLYDATA)

## Set meshing options.
#
print("Set meshing options ... ")
options = adaptive_mesher.create_options()
#help(sv.meshing.TetGenAdaptiveOptions)
#options.start_step = 100
#options.end_step = 100
options.step = 100

# options.use_isotropic_meshing = False; 

print("options values: ")
[ print("  {0:s}:{1:s}".format(key,str(value))) for (key, value) in sorted(options.get_values().items()) ]

## Generate an adpative mesh. 
#
results_file_name = 'all_results.vtu'
model_file_name = 'cylinder.vtp'
adaptive_mesher.generate_mesh(results_file=results_file_name, model_file=model_file_name, options=options)

#adaptive_mesher.load_model(file_name)

'''

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

'''