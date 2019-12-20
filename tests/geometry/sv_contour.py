
from pathlib import Path
import sv
import vtk

## Read an SV contour group file. 
#
def read_contours():
    home = str(Path.home())
    file_name = home + "/SimVascular/DemoProject/Segmentations/aorta.ctgr"
    #file_name = home + "/SimVascular/DemoProject/Segmentations/aorta.ctg"
    print("Read SV ctgr file: {0:s}".format(file_name))
    contour_group = sv.contour.Group(file_name)
    num_conts = contour_group.number_of_contours()
    contours = []

    for i in range(num_conts):
        cont = contour_group.get_contour(i)
        contours.append(cont)

    print("Number of contours: {0:d}".format(num_conts))
    return contours

def get_polydata(contour):
    return contour.get_polydata()
    '''
    coords = contour.get_contour_points()
    num_pts = len(coords)

    ## Create contour geometry points and line connectivity.
    #
    points = vtk.vtkPoints()
    points.SetNumberOfPoints(num_pts)
    lines = vtk.vtkCellArray()
    lines.InsertNextCell(num_pts)
    n = 0
    for pt in coords:
        points.SetPoint(n, pt[0], pt[1], pt[2])
        lines.InsertCellPoint(n)
        n += 1
    #_for pt in coords

    geom = vtk.vtkPolyData()
    geom.SetPoints(points)
    geom.SetLines(lines)
    return geom
    '''

