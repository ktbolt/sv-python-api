from pathlib import Path
import sv
import vtk

def create_contour_geometry(renderer, contour):
    """ 
    Create geometry for the contour points and control points.
    """
    coords = contour.get_contour_points()
    num_pts = len(coords)

    ## Create contour geometry points and line connectivity.
    #
    points = vtk.vtkPoints()
    points.SetNumberOfPoints(num_pts)
    lines = vtk.vtkCellArray()
    lines.InsertNextCell(num_pts+1)
    n = 0
    for pt in coords:
        points.SetPoint(n, pt[0], pt[1], pt[2])
        lines.InsertCellPoint(n)
        n += 1
    #_for pt in coords
    lines.InsertCellPoint(0)

    geom = vtk.vtkPolyData()
    geom.SetPoints(points)
    geom.SetLines(lines)
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(geom)
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetLineWidth(2.0)
    actor.GetProperty().SetColor(0.0, 0.6, 0.0)
    renderer.AddActor(actor)

    ## Add center point.
    #
    center = contour.get_center()
    num_pts = 1
    points = vtk.vtkPoints()
    vertices = vtk.vtkCellArray()
    pid = points.InsertNextPoint(center)
    vertices.InsertNextCell(1)
    vertices.InsertCellPoint(pid)
    points_pd = vtk.vtkPolyData()
    points_pd.SetPoints(points)
    points_pd.SetVerts(vertices)
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(points_pd)
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(1.0, 0.0, 0.0)
    actor.GetProperty().SetPointSize(5)
    renderer.AddActor(actor)

    ## Add control points.
    #
    coords = contour.get_control_points()
    num_pts = len(coords)
    points = vtk.vtkPoints()
    vertices = vtk.vtkCellArray()
    for pt in coords:
        pid = points.InsertNextPoint(pt)
        vertices.InsertNextCell(1)
        vertices.InsertCellPoint(pid)
    #_for pt in coords
    points_pd = vtk.vtkPolyData()
    points_pd.SetPoints(points)
    points_pd.SetVerts(vertices)
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(points_pd)
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(1.0, 0.0, 0.0)
    actor.GetProperty().SetPointSize(5)
    # renderer.AddActor(actor)


## Create renderer and graphics window.
renderer = vtk.vtkRenderer()
renderer_win = vtk.vtkRenderWindow()
renderer_win.AddRenderer(renderer)
renderer.SetBackground(0.8, 0.8, 0.8)
renderer_win.SetSize(500, 500)
renderer_win.Render()
renderer_win.SetWindowName("Vis SV Contours")

## Read an SV contour group file. 
#
home = str(Path.home())
file_name = home + "/SimVascular/DemoProject/Segmentations/aorta.ctgr"
#file_name = home + "/SimVascular/DemoProject/Segmentations/aorta.ctg"
print("Read SV ctgr file: {0:s}".format(file_name))
aorta_contours = sv.contour.Group(file_name)
num_conts = aorta_contours.number_of_contours()
print("Number of contours: {0:d}".format(num_conts))

for i in range(num_conts):
    cont = aorta_contours.get_contour(i)
    create_contour_geometry(renderer, cont)

## Create a trackball interacter to transoform the geometry using the mouse.
#
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
interactor.SetRenderWindow(renderer_win)
interactor.Start()


