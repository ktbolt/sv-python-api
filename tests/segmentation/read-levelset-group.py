''' Test reading in an SV contour group file for level set contours.
'''
from pathlib import Path
import sv
import sys
import vtk
sys.path.insert(1, '../graphics/')
import graphics as gr

## Read an SV segmentation group file. 
#
home = str(Path.home())
file_name = home + "/SimVascular/DemoProject/Segmentations/levelset.ctgr"
print("Read SV ctgr file: {0:s}".format(file_name))
aorta_segmentations = sv.segmentation.Group(file_name)
num_conts = aorta_segmentations.number_of_segmentations()
print("Number of segmentations: {0:d}".format(num_conts))

## Create renderer and graphics window.
win_width = 500
win_height = 500
renderer, renderer_window = gr.init_graphics(win_width, win_height)

## Show contours.
segs = []
for i in range(num_conts):
    print(" ")
    print("----------- Segmentation {0:d} -------- ".format(i))
    print("get_segmentation")
    seg = aorta_segmentations.get_segmentation(i)
    print("create_segmentation_geometry")
    gr.create_segmentation_geometry(renderer, seg)
    segs.append(seg)
    print("done ")

# Display window.
gr.display(renderer_window)

