import sv

print(dir(sv.segmentation))
print("Segmentation method names: {0:s}".format(str(sv.segmentation.Method.names)))

## Create CircleContour using factory.
#
ls_seg = sv.segmentation.create(sv.segmentation.Method.LEVEL_SET)
center = [0.0, 0.0, 0.0]

ls_seg = sv.segmentation.LevelSet()

