import contour 

print(dir(contour))
print("Contour kernel names: {0:s}".format(str(contour.kernel.names)))

## Create CircleContour using factory.
#
center = [0.0, 0.0, 0.0] 
cont = contour.create(contour.kernel.CIRCLE)
cont.set_center(center)
cont.set_radius(1.0)

## CircleContour using class.
#
cpt1 = [2.0, 0.0, 0.0] 
cpt2 = [3.0, 0.0, 0.0] 
radius = 1.0
circle_cont = contour.CircleContour()
circle_cont.add_control_point(cpt1)
circle_cont.add_control_point(cpt2)
circle_cont.set_radius(radius)
circle_cont.set_center(center)


## PolygonContour using class.
#
cpt1 = [2.0, 0.0, 0.0] 
cpt2 = [3.0, 0.0, 0.0] 
polygon_cont = contour.PolygonContour()


