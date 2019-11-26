'''
This scripts tests reading a PathGroup file.
'''
import sv 
#print(dir(sv.path_group))
#print(dir(sv.path_group.PathGroup))

## Create a PathGroup from an SV file.
#
file_name = "$HOME/DemoProject/Paths/aorta.pth"
aorta_group = sv.path_group.read(file_name)
print("Number of paths: {0:d}".format(aorta_group.get_time_size()))
print("Method: {0:s}".format(aorta_group.get_method()))
print("Path at time 0:")
aorta_path = aorta_group.get_path(0)
control_points = aorta_path.get_control_points()
print("  Number of control points: {0:d}".format(len(control_points)))
curve_points = aorta_path.get_curve_points()
print("  Number of curve points: {0:d}".format(len(curve_points)))

