'''
Test load mesh methods.

It is not clear what use it is to load a mesh. This might used for boundary layer
meshing?

'''
import sv
import vtk
from mesh_utils import setup_mesher

## Create a mesher and load a model.
mesher = setup_mesher(sv.meshing.Kernel.TETGEN)

## Load a mesh. 
file_name = 'cylinder-mesh.vtu'
mesher.load_mesh(file_name)

