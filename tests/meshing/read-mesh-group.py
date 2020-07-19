'''
This scipt tests reading in an SV Mesh from an .msh file.
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
demo_project = False
if demo_project:
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

## Get a mesh for time 0.
#
# Meshing parameter options are read from the .msh file.
#
mesher, options = mesh_group.get_mesh(0)
face_ids = mesher.get_model_face_ids()
print("Mesh face IDs: " + str(face_ids))

## Set options.
#options.mesh_wall_first = True
#options.radius_meshing_compute_centerlines = True

## Print options.
print("Options ... ")
[ print("  {0:s}:{1:s}".format(key,str(value))) for (key, value) in sorted(options.get_values().items()) ]

#sys.exit(0)

## Set wall face IDs.
if demo_project:
    face_ids = [1, 2]
else:
    face_ids = [1]
mesher.set_walls(face_ids)

## Generate the mesh. 
mesher.generate_mesh(options)

## Write the mesh.
#mesher.write_mesh(file_name=mesh_name+'.vtu')

#mesh_surface = mesher.get_surface()
#print("Number of surface mesh nodes: {0:d}".format(mesh_surface.GetNumberOfPoints()))

#mesh_model_polydata = mesher.get_model_polydata()
#print("Number of volume mesh nodes: {0:d}".format(mesh_model_polydata.GetNumberOfPoints()))

#face1_polydata = mesher.get_face_polydata(1)
#print("Face 1 number of nodes: {0:d}".format(face1_polydata.GetNumberOfPoints()))
#gr.add_geom(renderer, face1_polydata, color=[1.0, 0.0, 0.0], wire=False, edges=True)

#display(renderer_win)

