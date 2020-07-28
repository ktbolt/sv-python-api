''' This scripts tests reading a path planning .pth file.
'''
import sv 
import vtk 
import sys 
from pathlib import Path
sys.path.insert(1, '../graphics/')
import graphics as gr

## Create a Paths object from an SV file.
#
home = str(Path.home())
path_name = "aorta_subdivision"
path_name = "aorta"
file_name = home+"/Simvascular/DemoProject/Paths/" + path_name + ".pth"
paths = sv.pathplanning.Series(file_name)
print("Paths:")
print("  Number of time steps: {0:d}".format(paths.get_num_times()))

print(" ")
print("Path at time 0:")
aorta_path = paths.get_path(0)
control_points = aorta_path.get_control_points()
print("  Number of control points: {0:d}".format(len(control_points)))
curve_points = aorta_path.get_curve_points()
print("  Number of curve points: {0:d}".format(len(curve_points)))
#
point = aorta_path.get_curve_point(20)
print("  Point 20: {0:s}".format(str(point)))
tangent = aorta_path.get_curve_tangent(20)
print("  Tangent 20: {0:s}".format(str(tangent)))
normal = aorta_path.get_curve_normal(20)
print("  Normal 20: {0:s}".format(str(normal)))
#
num_subdiv = aorta_path.get_num_subdivisions()
print("  Number of subdivisions: {0:d}".format(num_subdiv))
subdiv_method = aorta_path.get_subdivision_method()
print("  Subdivision method: {0:s}".format(subdiv_method))

## Create renderer and graphics window.
win_width = 500
win_height = 500
renderer, renderer_window = gr.init_graphics(win_width, win_height)

# Create path geometry.
gr.create_path_geometry(renderer, aorta_path)

# Display window.
gr.display(renderer_window)


