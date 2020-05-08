from pathlib import Path
import sv

#print(dir(sv))
#print(dir(sv.segmentation))

## Read an SV segmentation group file. 
#
home = str(Path.home())
file_name = home + "/SimVascular/DemoProject/Segmentations/aorta.ctgr"
#file_name = home + "/SimVascular/DemoProject/Segmentations/aorta.ctg"
print("Read SV ctgr file: {0:s}".format(file_name))
aorta_segmentations = sv.segmentation.Group(file_name)
num_segs = aorta_segmentations.number_of_segmentations()
print("Number of segmentations: {0:d}".format(num_segs))

## Get segmentations.
#
segmentations = []
for i in range(num_segs):
    print("---------- segmentation {0:d} ----------".format(i))
    seg = aorta_segmentations.get_segmentation(i)
    #segmentations.append(cont)
    center = seg.get_center()
    path_point = seg.get_path_point()
    control_points = seg.get_control_points()
    segmentation_points = seg.get_points()
    print("Type: {0:s}".format(seg.get_type()))
    print("Center: {0:s}".format(str(center)))
    print("Path point: {0:s}".format(str(path_point)))
    print("Number of control points: {0:d}".format(len(control_points)))
    #for i,pt in enumerate(control_points): 
    #    print("  Control point {0:d}: {1:s}".format(i+1, str(pt)))
    print("Number of segmentation points: {0:d}".format(len(segmentation_points)))
    #for i,pt in enumerate(segmentation_points): 
    #    print("Contour point {0:d}: {1:s}".format(i+1, str(pt)))

