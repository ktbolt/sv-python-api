import sv

print(dir(sv.segmentation))
print("segmentation kernel names: {0:s}".format(str(sv.segmentation.Method.names)))

## Create Threshold object using factory.
#
cont = sv.segmentation.create(sv.segmentation.Method.THRESHOLD)
center = [0.0, 0.0, 0.0]

cont = sv.segmentation.Threshold()

