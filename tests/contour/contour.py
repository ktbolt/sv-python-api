import sv

print(dir(sv.contour))
print("Contour kernel names: {0:s}".format(str(sv.contour.Kernel.names)))
print("Contour kernel circle: {0:s}".format(str(sv.contour.Kernel.CIRCLE)))

## Create Contour. 
#
cont = sv.contour.Contour()

