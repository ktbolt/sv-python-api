'''
Test the sv.geometry.LoftOptions() class. 
'''
from pathlib import Path
import sv
import vtk

loft_options = sv.geometry.LoftOptions()
print(dir(loft_options))

print("num_pts: {0:d}".format(loft_options.num_pts))
loft_options.num_pts = 20
print("num_pts: {0:d}".format(loft_options.num_pts))

