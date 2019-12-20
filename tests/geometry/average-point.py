'''
Test the geometry.sv.geometry.average_point method.
'''
from pathlib import Path
import sv
import vtk
import graphics as gr
import sv_contour 

win_width = 500
win_height = 500
renderer, renderer_window = gr.init_graphics(win_width, win_height)

## Read contours.
contours = sv_contour.read_contours()
contour = contours[10]
center = contour.get_center()
contour_polydata = contour.get_polydata()
gr.create_contour_geometry(renderer, contour)
print("contour_polydata type: " + str(type(contour_polydata)))

print("Create a cylinder.")
kernel = sv.solid.Kernel.POLYDATA
modeler = sv.solid.Modeler(kernel)
center = [0.0, 0.0, 0.0]
axis = [0.0, 0.0, 1.0]
radius = 1.5
length = 10.0
cylinder = modeler.cylinder(radius, length, center, axis)
cylinder_polydata = cylinder.get_polydata()
gr.add_geom(renderer, cylinder_polydata, color=[1.0, 0.0, 0.0], wire=True)

## Compute average point. 
avg_point = sv.geometry.average_point(cylinder_polydata)
#avg_point = sv.geometry.average_point(contour_polydata)

sphere = vtk.vtkSphereSource()
sphere.SetCenter(avg_point[0], avg_point[1], avg_point[2])
sphere.SetRadius(0.2)
sphere.Update()
sphere_pd = sphere.GetOutput()
gr.add_geom(renderer, sphere_pd, color=[1.0, 1.0, 1.0])

## Show geometry.
#
camera = renderer.GetActiveCamera();
camera.Zoom(0.5)
#camera.SetPosition(center[0], center[1], center[2])
camera.SetFocalPoint(center[0], center[1], center[2])
gr.display(renderer_window)

