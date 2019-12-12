import sv
import vtk
import sys

#print(dir(sv))
print(dir(sv.solid))
print("Solid modeling kernel names: {0:s}".format(str(sv.solid.Kernel.names)))

## Check that the modeler for the given kernel exists.
#
if not sv.solid.modeler_exists(sv.solid.Kernel.PARASOLID):
    print("No solid modeler for kernel: {0:s}".format(sv.solid.Kernel.PARASOLID))
    sys.exit(1)

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
print("Cylinder: num cells: {0:d}".format(cyl_polydata.GetNumberOfCells()))

