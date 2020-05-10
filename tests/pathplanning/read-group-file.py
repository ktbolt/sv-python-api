''' This scripts tests reading a PathGroup file.
'''
import sv 
import vtk 
import sys 
from pathlib import Path
sys.path.insert(1, '../graphics/')
import graphics as gr

## Create a PathGroup from an SV file.
#
home = str(Path.home())
path_name = "aorta"
path_name = "aorta_subdivision"
file_name = home+"/Simvascular/DemoProject/Paths/" + path_name + ".pth"
aorta_group = sv.pathplanning.Group(file_name)
print("Path group:")
print("  Number of paths: {0:d}".format(aorta_group.get_num_paths()))
# These are no longer exposed.
#print("  Method: {0:s}".format(aorta_group.get_method()))
#calc_number = aorta_group.get_calculation_number()
#print("  Calculation number: {0:d}".format(calc_number))

print(" ")
print("Path at time 0:")
aorta_path = aorta_group.get_path(0)
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


