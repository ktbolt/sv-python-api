import contour 

print(dir(contour))

#print(contour.cos_func(1.0))

## Contour 
#
cont = contour.Contour()
center = [0.0, 0.0, 0.0] 
cont.set_center(center)
pt = [1.0, 0.0, 0.0] 
cont.add_control_point(pt)

## CircleContour 
#
cpt1 = [2.0, 0.0, 0.0] 
cpt2 = [3.0, 0.0, 0.0] 
radius = 1.0
circle_cont = contour.CircleContour()
circle_cont.add_control_point(cpt1)
circle_cont.add_control_point(cpt2)
circle_cont.set_radius(radius)
circle_cont.set_center(center)

print("---------------------------")

'''
print(contour.kernel)
print(contour.kernel.circle)

if "circle" == contour.kernel.circle:
    print("------------------ true ---------------------------")
else:
    print("------------------ false ---------------------------")
'''



