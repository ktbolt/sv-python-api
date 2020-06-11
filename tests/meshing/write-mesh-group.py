'''
This scipt tests writing an SV Mesh group to a .msh file.
'''
from pathlib import Path
import sv
import sys
import vtk
sys.path.insert(1, '../graphics/')
import graphics as gr

## Read an SV mesh group file. 
#
home = str(Path.home())

## Demo project tests.
if False:
    project_name = "DemoProject"
    mesh_name = "demo"
    mesh_name = "demo-sphere-refine"
    mesh_name = "demo-local-edge-and-sphere"
    mesh_name = "demo-local-edge-and-radius" 
    mesh_name = "demo-refine-all"

# CylinderProject tests.
else:
    project_name = "CylinderProject"
    mesh_name = "cylinder"

file_name = home + "/SimVascular/" + project_name + "/Meshes/" + mesh_name + ".msh"
print("Read SV msh file: {0:s}".format(file_name))
mesh_group = sv.meshing.Group(file_name)
num_meshes = mesh_group.get_num_meshes()
print("Number of meshes: {0:d}".format(num_meshes))

## Write a mesh group.
file_name = mesh_name + "-test.msh"
mesh_group.write(file_name)

