import sv

print(dir(sv.segmentation))
print("Segmentation method names: {0:s}".format(str(sv.segmentation.Method.names)))

## Create Circle using factory.
#
cont = sv.segmentation.create(sv.segmentation.Method.POLYGON)
center = [0.0, 0.0, 0.0]

cont = sv.segmentation.Polygon()

