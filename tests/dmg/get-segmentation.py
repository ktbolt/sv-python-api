'''
Test getting a segmentation from the SV Data Manager.

This is tested using the Demo Project.
'''

import sv
  
## Create a Python contour group object from the SV Data Manager 'Segmentations/aorta' node. 
#
seg_name = "aorta"
contour_group = sv.dmg.get_contour(seg_name)
num_conts = contour_group.number_of_contours()
print("Number of contours: {0:d}".format(num_conts))

## Get contours.
#
'''
for i in range(num_conts):
    print("---------- contour {0:d} ----------".format(i))
    cont = contour_group.get_contour(i)
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
'''



