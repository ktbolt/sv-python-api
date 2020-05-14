''' Test creating a circle segmentation using a plane.
'''
import sv
import sys
import vtk
sys.path.insert(1, '../graphics/')
import graphics as gr

## Create a segmentation using the Circle class. 
#
print("Create circle segmentation ...")
radius = 1.0
center = [0.0, 0.0, 0.0]
#
plane = vtk.vtkPlane()
plane_center = [10.0, 0.0, 0.0]
plane.SetOrigin(plane_center);
plane_normal = [0.0, 1.0, 0.0]
plane.SetNormal(plane_normal)
#
segmentation = sv.segmentation.Circle(radius=radius, plane=plane)
center = segmentation.get_center()
print("  Center: {0:g} {1:g} {2:g}".format(center[0], center[1], center[2]))
#
control_points = segmentation.get_control_points()
num_control_pts = len(control_points)
print("  Number of control_points: {0:d}".format(num_control_pts))
#
points = segmentation.get_points()
num_pts = len(points)
print("  Number of points: {0:d}".format(num_pts))

## Create renderer and graphics window.
win_width = 500
win_height = 500
renderer, renderer_window = gr.init_graphics(win_width, win_height)

## Show plane.
gr.add_plane(renderer, plane_center, plane_normal, color=[1,0,1])

## Show contour.
gr.create_segmentation_geometry(renderer, segmentation)

# Display window.
gr.display(renderer_window)


