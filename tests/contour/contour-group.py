from pathlib import Path
import sv

#print(dir(sv))
print(dir(sv.contour))

## Read an SV contour group file. 
#
home = str(Path.home())
file_name = home + "/SimVascular/DemoProject/Segmentations/aorta.ctgr"
#file_name = home + "/SimVascular/DemoProject/Segmentations/aorta.ctg"
print("Read SV ctgr file: {0:s}".format(file_name))
aorta_contours = sv.contour.Group(file_name)
num_conts = aorta_contours.number_of_contours()
print("Number of contours: {0:d}".format(num_conts))

## Get contours.
#
contours = []
for i in range(num_conts):
    print("---------- contour {0:d} ----------".format(i))
    cont = aorta_contours.get_contour(i)
    #contours.append(cont)
    center = cont.get_center()
    path_point = cont.get_path_point()
    control_points = cont.get_control_points()
    contour_points = cont.get_contour_points()
    print("Type: {0:s}".format(cont.get_type()))
    print("Center: {0:s}".format(str(center)))
    print("Path point: {0:s}".format(str(path_point)))
    print("Number of control points: {0:d}".format(len(control_points)))
    #for i,pt in enumerate(control_points): 
    #    print("  Control point {0:d}: {1:s}".format(i+1, str(pt)))
    print("Number of contour points: {0:d}".format(len(contour_points)))
    #for i,pt in enumerate(contour_points): 
    #    print("Contour point {0:d}: {1:s}".format(i+1, str(pt)))

