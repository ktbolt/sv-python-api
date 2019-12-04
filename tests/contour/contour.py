import sv

print(dir(sv.contour))
print("Contour kernel names: {0:s}".format(str(sv.contour.Kernel.names)))

## Create CircleContour using factory.
#
circle_cont_1 = sv.contour.create(sv.contour.Kernel.CIRCLE)
#circle_cont = sv.contour.create("bob")
center = [0.0, 0.0, 0.0]
#circle_cont.set_center(center)
circle_cont_1.set_radius(1.0)

circle_cont_2 = sv.contour.Circle()
circle_cont_2.set_radius(1.0)

