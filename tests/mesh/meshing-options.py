'''
Test the sv.meshing.MeshingOptions() class. 
'''
from pathlib import Path
import sv
import vtk

meshing_options = sv.meshing.MeshingOptions()
print(dir(meshing_options))

print("meshing_options.surface_mesh_flag: " + str(meshing_options.surface_mesh_flag))


