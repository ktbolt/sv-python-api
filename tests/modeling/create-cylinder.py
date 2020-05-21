''' Test creating a cylinder.
'''
import sv
import sys
import vtk
sys.path.insert(1, '../graphics/')
import graphics as gr

# Create a modeler.
oc_modeler = sv.modeling.Modeler(sv.modeling.Kernel.OPENCASCADE)
modeler = sv.modeling.Modeler(sv.modeling.Kernel.POLYDATA)

## Create a cylinder.
print("Create a cylinder ...")
center = [0.0, 0.0, 0.0]
axis = [0.0, 1.0, 0.0]
axis = [1.0, 0.0, 0.0]
radius = 2.0 
length = 4.0 
cylinder = modeler.cylinder(center=center, axis=axis, radius=radius, length=length)
print("  Cylinder type: " + str(type(cylinder)))
cylinder_pd = cylinder.get_polydata()
print("  Cylinder: num nodes: {0:d}".format(cylinder_pd.GetNumberOfPoints()))
#
oc_cylinder = oc_modeler.cylinder(center=center, axis=axis, radius=radius, length=length)
print("  OC Cylinder type: " + str(type(oc_cylinder)))
oc_cylinder_pd = oc_cylinder.get_polydata()
print("  OC Cylinder: num nodes: {0:d}".format(oc_cylinder_pd.GetNumberOfPoints()))

## Create renderer and graphics window.
win_width = 500
win_height = 500
renderer, renderer_window = gr.init_graphics(win_width, win_height)

## Add model polydata.
gr.add_geometry(renderer, cylinder_pd, color=[0.0, 1.0, 0.0], wire=True, edges=False)
#gr.add_geometry(renderer, oc_cylinder_pd, color=[1.0, 0.0, 0.0], wire=True, edges=False)

## Add a sphere.
gr.add_sphere(renderer, center=center, radius=0.1, color=[1.0, 1.0, 1.0], wire=True)

pt1 = center
pt2 = [ center[i] + length/2.0 * axis[i] for i in range(3) ]
gr.add_line(renderer, pt1, pt2, color=[0.5, 0.0, 0.0], width=4)

# Display window.
gr.display(renderer_window)



