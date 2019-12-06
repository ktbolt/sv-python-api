import sv

print(dir(sv.contour))
print("Contour kernel names: {0:s}".format(str(sv.contour.Kernel.names)))

## Create Contour. 
#
cont = sv.contour.Contour()

