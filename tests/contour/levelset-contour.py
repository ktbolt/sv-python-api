import sv

print(dir(sv.contour))
print("Contour kernel names: {0:s}".format(str(sv.contour.Kernel.names)))

## Create CircleContour using factory.
#
cont = sv.contour.create(sv.contour.Kernel.LEVEL_SET)
center = [0.0, 0.0, 0.0]

cont = sv.contour.LevelSet()
