'''
Test sv.math methods.
'''
import sv
import vtk
import math 

## Curve length.
#
points = [ [0.0, 0.0, 0.0], [1.0, 0.0, 0.0] ]
curve_length = sv.math.curve_length(points)
print("Curve length: {0:g}".format(curve_length))



