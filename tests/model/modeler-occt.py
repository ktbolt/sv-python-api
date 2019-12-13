import sv
import vtk

#print(dir(sv))
print(dir(sv.solid))
print("Solid modeling kernel names: {0:s}".format(str(sv.solid.Kernel.names)))

## Create a polydata modeler.
#
modeler = sv.solid.Modeler(sv.solid.Kernel.OPENCASCADE)

## Create a cylinder.
#
print("Create a cylinder ...") 
center = [0.0, 0.0, 0.0]
axis = [0.0, 0.0, 1.0]
radius = 1.5
length = 10.0
cyl = modeler.cylinder(radius, length, center, axis)
print("cyl type: " + str(type(cyl)))
cyl_polydata = cyl.get_polydata() 
print("Cylinder: num nodes: {0:d}".format(cyl_polydata.GetNumberOfPoints()))

