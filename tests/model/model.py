import sv
import vtk

#print(dir(sv))
print(dir(sv.solid))
print("Solid modeling kernel names: {0:s}".format(str(sv.solid.Kernel.names)))

## Create model. 
#
#model = sv.solid.SolidModel()
#model = sv.solid.SolidModel("bob")
#model = sv.solid.SolidModel(sv.solid.Kernel.PARASOLID)

#model = sv.solid.PolyData()

#model = sv.solid.Solid(sv.solid.Kernel.POLYDATA)

#print("Model type: {0:s}".format(str(type(model))))

## Create a cylinder.
#
print("Create a cylinder.") 
center = [0.0, 0.0, 0.0]
axis = [0.0, 0.0, 1.0]
radius = 1.5
length = 10.0
model = sv.solid.Solid(sv.solid.Kernel.POLYDATA)
model.cylinder(radius, length, center, axis)
cyl_polydata = model.get_polydata() 
print("polydata: " + str(type(cyl_polydata)))
print("Cylinder: num nodes: {0:d}".format(cyl_polydata.GetNumberOfPoints()))

