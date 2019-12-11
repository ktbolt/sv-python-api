import sv
import vtk

print(dir(sv))

## Create a polydata modeler.
#
modeler = sv.solid.Modeler(sv.solid.Kernel.PARASOLID)

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

