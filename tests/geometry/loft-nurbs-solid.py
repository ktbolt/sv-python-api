from pathlib import Path
import sv
import vtk
import graphics as gr
import sv_contour 

win_width = 500
win_height = 500
renderer, renderer_window = gr.init_graphics(win_width, win_height)
radius = 0.05

## Read contours.
contours = sv_contour.read_contours()

## Set list of contours to loft.
#
# [TODO] Some values of num_out_pts_in_segs produces bad surfaces.
#
# num_out_pts_in_segs = 100   good
# num_out_pts_in_segs = 60    bad
# num_out_pts_in_segs = 50    bad
# num_out_pts_in_segs = 40    bad
# num_out_pts_in_segs = 30    bad
# num_out_pts_in_segs = 25    good
# num_out_pts_in_segs = 20    good
# num_out_pts_in_segs = 10    good
num_out_pts_in_segs = 25    
num_out_pts_along_length = 12 
num_linear_pts_along_length = 12

# [TODO] use_distance = False does not work.
#use_distance = False
use_distance = True

contour1 = contours[10]
center = contour1.get_center()
contour1_polydata = contour1.get_polydata()
contour1_ipolydata = sv.geometry.interpolate_closed_curve(polydata=contour1_polydata, number_of_points=num_out_pts_in_segs)
gr.add_geom(renderer, contour1_ipolydata, color=[0.5, 0.5, 0.0])
gr.create_contour_geometry(renderer, contour1)

contour2 = contours[11]
contour2_polydata = contour2.get_polydata()
contour2_ipolydata = sv.geometry.interpolate_closed_curve(polydata=contour2_polydata, number_of_points=num_out_pts_in_segs)
gr.create_contour_geometry(renderer, contour2)
#gr.add_geom(renderer, contour2_ipolydata, color=[0.5, 0.5, 0.0])

contour3 = contours[12]
contour3_polydata = contour3.get_polydata()
contour3_ipolydata = sv.geometry.interpolate_closed_curve(polydata=contour3_polydata, number_of_points=num_out_pts_in_segs)
gr.create_contour_geometry(renderer, contour3)

# Align contours.
#
contour_list = [] 
contour_list.append(contour1_ipolydata) 

contour2_polydata_align = sv.geometry.align_profile(contour1_ipolydata, contour2_ipolydata, use_distance=use_distance)
#contour2_polydata_align = sv.geometry.interpolate_closed_curve(polydata=contour2_polydata_align, number_of_points=num_out_pts_in_segs)
contour_list.append(contour2_polydata_align) 
#gr.add_geom(renderer, contour2_polydata_align, color=[0.5, 0.5, 0.0])

contour3_polydata_align = sv.geometry.align_profile(contour2_polydata_align, contour3_ipolydata, use_distance=use_distance)
#contour3_polydata_align = sv.geometry.interpolate_closed_curve(polydata=contour3_polydata_align, number_of_points=num_out_pts_in_segs)
contour_list.append(contour3_polydata_align) 

pt = 3*[0.0]
contour1_ipolydata.GetPoints().GetPoint(0, pt)
gr.add_sphere(renderer, pt, radius)
contour1_ipolydata.GetPoints().GetPoint(4, pt)
gr.add_sphere(renderer, pt, radius, color=[0,1,0])

pt = 3*[0.0]
contour2_polydata_align.GetPoints().GetPoint(0, pt)
gr.add_sphere(renderer, pt, radius)
contour2_polydata_align.GetPoints().GetPoint(4, pt)
gr.add_sphere(renderer, pt, radius, color=[0,1,0])

#contour3_polydata_align.GetPoints().GetPoint(0, pt)
#gr.add_sphere(renderer, pt, radius)
#contour3_polydata_align.GetPoints().GetPoint(4, pt)
#gr.add_sphere(renderer, pt, radius, color=[0,1,0])


## Loft solid. 
#
loft_options = sv.geometry.LoftNurbsOptions()
loft_options.u_degree = 4; 
loft_options.v_degree = 4; 

loft_solid = sv.geometry.loft_solid_using_nurbs(polydata_list=contour_list, loft_nurbs_options=loft_options)
#gr.add_geom(renderer, loft_solid, color=[0.5, 0.0, 0.0], wire=True)

## Show geometry.
#
camera = renderer.GetActiveCamera();
camera.Zoom(0.5)
#camera.SetPosition(center[0], center[1], center[2])
camera.SetFocalPoint(center[0], center[1], center[2])
gr.display(renderer_window)

