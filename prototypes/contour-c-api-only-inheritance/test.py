
import contour 
import path 
import vtk

#print(dir(path))

## Create a Path .
#
cpt1 = [2.0, 0.0, 0.0] 
cpt2 = [3.0, 0.0, 0.0] 
cpt3 = [4.0, 0.0, 0.0] 
cpt4 = [5.0, 0.0, 0.0] 
path = path.Path()
path.add_control_point(cpt1)
path.add_control_point(cpt2)
path.add_control_point(cpt3)
path.add_control_point(cpt4)

## Create CircleContour from path.
#
circle_cont = contour.CircleContour()
circle_cont.set_center_from_path(path, 2)
#circle_cont.set_center_from_path(2, path)


