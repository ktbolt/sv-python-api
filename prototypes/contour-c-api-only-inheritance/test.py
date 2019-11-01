import contour

print(dir(contour))

#print(contour.cos_func(1.0))

## Contour 
cont = contour.Contour()
pt = [1.0, 0.0, 0.0] 
cont.add_control_point(pt)

## CircleContour 
cpt1 = [2.0, 0.0, 0.0] 
cpt2 = [3.0, 0.0, 0.0] 
circle_cont = contour.CircleContour()
circle_cont.add_control_point(cpt1)
circle_cont.add_control_point(cpt2)

