import sv
import vtk

#print(dir(sv))
print(dir(sv.solid))
print("Solid modeling kernel names: {0:s}".format(str(sv.solid.Kernel.names)))

## Create a polydata modeler.
#
modeler = sv.solid.Modeler(sv.solid.Kernel.POLYDATA)

## Create a cylinder.
#
print("Create a cylinder ...") 
center = [0.0, 0.0, 0.0]
axis = [0.0, 0.0, 1.0]
radius = 1.5
length = 10.0
cyl = modeler.cylinder(radius, length, center, axis)
print("cyl type: " + str(type(cyl)))
print(cyl.available())
cyl_polydata = cyl.get_polydata() 
print("Cylinder: num nodes: {0:d}".format(cyl_polydata.GetNumberOfPoints()))

## Create a box.
#
print("Create a box ...")
center = [0.0, 0.0, 0.0]
box = modeler.box(center, length=3.0, height=1.0, width=2.0)
#box = modeler.box3d(center)
#box = modeler.box3d(center, length=3.0)
#box = modeler.box3d(center, width, height, length)
print("box type: " + str(type(box)))
box_polydata = box.get_polydata()
print("Box: num nodes: {0:d}".format(box_polydata.GetNumberOfPoints()))

