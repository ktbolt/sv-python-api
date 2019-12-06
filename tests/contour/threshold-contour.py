import sv

print(dir(sv.contour))
print("Contour kernel names: {0:s}".format(str(sv.contour.Kernel.names)))

## Create Threshold object using factory.
#
cont = sv.contour.create(sv.contour.Kernel.THRESHOLD)
center = [0.0, 0.0, 0.0]

cont = sv.contour.Threshold()

