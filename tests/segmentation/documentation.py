# Test the 'segmentation' module documentation.
#
import sv
import pydoc

#help(dir(sv))

#help(sv.segmentation)

#help(sv.segmentation.Circle)
#print(dir(sv.segmentation.Circle))
#print(dir(sv.segmentation.Circle))
#print(sv.segmentation.Circle.__doc__)
#print(sv.segmentation.Circle.get_center.__doc__)
class_names = [f for f in dir(sv.segmentation.Circle) if not f.startswith('_')]
print(class_names)

write_docs = True
write_docs = False

if write_docs:
    pydoc.writedoc("sv.segmentation.Circle")
    pydoc.writedoc("sv.segmentation.Contour")
    pydoc.writedoc("sv.segmentation.Polygon")
    pydoc.writedoc("sv.segmentation.SplinePolygon")

