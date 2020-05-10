''' This scripts tests creating a PathGroup and writing it to a .pth file.
'''
import json 
import sv 

## Create a PathGroup.
aorta_group = sv.pathplanning.Group()

## Create Path object.
path = sv.pathplanning.Path()

# Read control points.
with open('aorta-control-points.json') as json_file:
    control_points = json.load(json_file)

# Add control points.
for pt in control_points:
    path.add_control_point(pt)

## Add path to group.
aorta_group.set_path(path=path, time=0)
aorta_group.set_path_id(1)

print("Path group:")
print("  Number of paths: {0:d}".format(aorta_group.get_num_paths()))

## Write the path group to a file.
aorta_group.write("test-group.pth")

