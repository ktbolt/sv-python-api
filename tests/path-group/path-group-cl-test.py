'''
This scripts tests reading a PathGroup file.
'''
from pathlib import Path
import sv 
print(dir(sv.path))

## Create a PathGroup from an SV file.
#
home = str(Path.home())
file_name = home + "/SimVascular/DemoProject/Paths/aorta.pth"
aorta_group = sv.path.Group(file_name)

print("Number of paths: {0:d}".format(aorta_group.get_time_size()))
print("Method: {0:s}".format(aorta_group.get_method()))

## Get the path at time 0.
print("Path at time 0:")
aorta_path = aorta_group.get_path(0)

## Get control and curve points.
control_points = aorta_path.get_control_points()
print("  Number of control points: {0:d}".format(len(control_points)))
curve_points = aorta_path.get_curve_points()
print("  Number of curve points: {0:d}".format(len(curve_points)))

## Test path calculatio method class.
print("Path calculation method names: {0:s}".format(str(sv.path.CalculationMethod.names)))
aorta_group.set_method(sv.path.CalculationMethod.TOTAL)



