''' Test creating a path.
'''
import json
import sv 
import sys
sys.path.insert(1, '../graphics/')
import graphics as gr

# Read control points.
with open('aorta-control-points.json') as json_file:
    control_points = json.load(json_file)

# Create Path object.
#path = sv.path.Path()
#path = sv.path_planning.Path()
path = sv.pathplanning.Path()

# Add control points.
for pt in control_points:
    path.add_control_point(pt)

print("Path:")
num_subdiv = path.get_num_subdivisions()
subdiv_method = path.get_subdivision_method()
print("  Number of subdivisions: {0:d}".format(num_subdiv))
print("  Subdivision method: {0:s}".format(subdiv_method))

# Get control points.
control_points = path.get_control_points()
print("Number of control points: {0:d}".format(len(control_points)))

# Get path curve.
curve_polydata = path.get_curve_polydata()
print("Curve polydata: ")
print("  Number of points: {0:d}".format(curve_polydata.GetNumberOfPoints()))

# Create graphics window.
win_width = 500
win_height = 500
renderer, renderer_window = gr.init_graphics(win_width, win_height)

# Show path.
gr.create_path_geometry(renderer, path)
#gr.add_geometry(renderer, curve_polydata)

# Display window.
gr.display(renderer_window)


