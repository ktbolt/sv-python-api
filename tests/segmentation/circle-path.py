''' Test creating a circle segmentation using a path.
'''
import json
import sv
import sys
import vtk
sys.path.insert(1, '../graphics/')
import graphics as gr

def create_segmentation(renderer, path, path_index):
    print("Create segmentation ...")    

    ## Create a segmentation.
    print("Circle segmentation: ")
    radius = 1.0

    # Get path curve frame.
    print("  Path index: " + str(path_index))    
    curve_frame = path.get_curve_frame(path_index)
    print("Path curve frame: ")
    print("  ID: " + str(curve_frame.id))    
    print("  Position: " + str(curve_frame.position))    
    print("  Normal: " + str(curve_frame.normal))    
    print("  Tangent: " + str(curve_frame.tangent))    

    # Create circle segmentation.
    segmentation = sv.segmentation.Circle(radius=radius, frame=curve_frame)

    center = segmentation.get_center()
    print("  Center: {0:g} {1:g} {2:g}".format(center[0], center[1], center[2]))
    control_points = segmentation.get_control_points()
    print("  Control_points: ")
    print("    1: {0:s}".format(str(control_points[0])))
    print("    2: {0:s}".format(str(control_points[1])))

    return segmentation 

def create_path():
    # Read control points.
    with open('../pathplanning/aorta-control-points.json') as json_file:
        control_points = json.load(json_file)

    # Create Path object.
    #path = sv.path.Path()
    #path = sv.path_planning.Path()
    path = sv.pathplanning.Path()

    # Add control points.
    for pt in control_points:
        path.add_control_point(pt)

    return path

## Create a path.
path = create_path()

## Create renderer and graphics window.
win_width = 500
win_height = 500
renderer, renderer_window = gr.init_graphics(win_width, win_height)

## Create a segmentation at path index 5.
seg1 = create_segmentation(renderer, path, path_index=5)

## Show segmentation.
gr.create_segmentation_geometry(renderer, seg1, color=[1.0, 0.0, 0.0])
print("Set radius ...")

## Change segmentation radius.
seg1.set_radius(2.0)
gr.create_segmentation_geometry(renderer, seg1, color=[1.0, 0.0, 1.0])
radius = seg1.get_radius()
print("  Radius: {0:g}".format(radius))

## Change segmentation frame.
curve_frame = path.get_curve_frame(10)
print("New segmentation center: {0:s}".format(str(curve_frame.position)))
seg1.set_frame(frame=curve_frame)
gr.create_segmentation_geometry(renderer, seg1, color=[0.0, 1.0, 1.0])
gr.add_sphere(renderer, curve_frame.position, 0.2, color=[1.0, 1.0, 0.0], wire=True)

# Show path.
gr.create_path_geometry(renderer, path)

## Add a sphere at the origin.
gr.add_sphere(renderer, [0.0,0.0,0.0], 0.5, color=[1.0, 1.0, 1.0], wire=True)

# Display window.
gr.display(renderer_window)


