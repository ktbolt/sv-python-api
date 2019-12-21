'''
Test aligining two profiles.
'''
from pathlib import Path
import sv
import vtk
import graphics as gr
import sv_contour 

radius = 0.05
win_width = 500
win_height = 500
renderer, renderer_window = gr.init_graphics(win_width, win_height)

num_samples = 20

## Read contours.
contours = sv_contour.read_contours()

contour1 = contours[10]
center = contour1.get_center()
points1 = contour1.get_contour_points()
cpoints1 = contour1.get_control_points()
contour1_polydata = contour1.get_polydata()
gr.create_contour_geometry(renderer, contour1)
contour1_ipolydata = sv.geometry.interpolate_closed_curve(polydata=contour1_polydata, number_of_points=num_samples)
pt = 3*[0.0]
contour1_ipolydata.GetPoints().GetPoint(0, pt)
gr.add_sphere(renderer, pt, radius, color=[1,0,0])
contour1_ipolydata.GetPoints().GetPoint(4, pt)
gr.add_sphere(renderer, pt, radius, color=[0,1,0])

contour2 = contours[11]
points2 = contour2.get_contour_points()
cpoints2 = contour2.get_control_points()
contour2_polydata = contour2.get_polydata()
gr.create_contour_geometry(renderer, contour2)
contour2_ipolydata = sv.geometry.interpolate_closed_curve(polydata=contour2_polydata, number_of_points=num_samples)

contour2_align_polydata = sv.geometry.align_profile(contour1_ipolydata, contour2_ipolydata, use_distance=True)
#contour2_align_polydata = sv.geometry.interpolate_closed_curve(polydata=contour2_align_polydata, number_of_points=num_samples)
pt = 3*[0.0]
contour2_align_polydata.GetPoints().GetPoint(0, pt)
gr.add_sphere(renderer, pt, radius, color=[1,0,0])
contour2_align_polydata.GetPoints().GetPoint(4, pt)
gr.add_sphere(renderer, pt, radius, color=[0,1,0])


## Show geometry.
#
camera = renderer.GetActiveCamera();
camera.Zoom(0.5)
#camera.SetPosition(center[0], center[1], center[2])
camera.SetFocalPoint(center[0], center[1], center[2])
gr.display(renderer_window)

