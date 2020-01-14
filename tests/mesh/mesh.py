import sv
import vtk

#print(dir(sv))
print(dir(sv.meshing))
print("Mesh generation kernel names: {0:s}".format(str(sv.meshing.Kernel.names)))

## Create a TetGen mesher.
#
mesher = sv.meshing.MeshGenerator(sv.meshing.Kernel.TETGEN)

