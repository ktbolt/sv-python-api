import sv

print(dir(sv.segmentation))
print("segmentation method names: {0:s}".format(str(sv.segmentation.Method.names)))

## Create CircleContour using factory.
#
cont = sv.segmentation.create(sv.segmentation.Method.SPLINE_POLYGON)
center = [0.0, 0.0, 0.0]

cont = sv.segmentation.SplinePolygon()

