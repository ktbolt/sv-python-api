import sv

print(dir(sv.contour))
print("Contour kernel names: {0:s}".format(str(sv.contour.kernel.names)))

## Create CircleContour using factory.
#
#center = [0.0, 0.0, 0.0]
cont = sv.contour.create(sv.contour.kernel.CIRCLE)
#cont.set_center(center)
#cont.set_radius(1.0)

