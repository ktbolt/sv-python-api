'''
Test adding a segmentation to the SV Data Manager.

This is tested using the Demo Project.
'''
from pathlib import Path
import sv

## Create a PathGroup from an SV file.
#
# Read an SV contour group file. 
#
home = str(Path.home())
file_name = home + "/SimVascular/DemoProject/Segmentations/aorta.ctgr"
print("Read SV ctgr file: {0:s}".format(file_name))
aorta_contours = sv.contour.Group(file_name)
num_conts = aorta_contours.number_of_contours()
print("Number of contours: {0:d}".format(num_conts))
contours = []
for i in range(num_conts):
    #print("---------- contour {0:d} ----------".format(i))
    contour = aorta_contours.get_contour(i)
    contours.append(contour)

## Add the Python contour objects under the SV Data Manager 'Segmentations' nodes
#  as a new  node named 'new_aorta'.
#
sv.dmg.add_contour(name="new_aorta", path="aorta", contours=contours)

