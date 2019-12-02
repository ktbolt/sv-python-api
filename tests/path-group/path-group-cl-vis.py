'''
This scripts tests reading a PathGroup file.
'''
import sv 
import vtk 
from pathlib import Path
#print(dir(sv.path_group))
#print(dir(sv.path_group.PathGroup))

def create_path_geometry(renderer, path):
    """ Create geometry for the path curve and control points.
    """
    coords = path.get_curve_points()
    num_pts = len(coords)

    # Create contour geometry points and line connectivity.
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
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(geom)
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetLineWidth(2.0)
    actor.GetProperty().SetColor(0.0, 0.6, 0.0)
    renderer.AddActor(actor)

    ## Add control points.
    coords = path.get_control_points()
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
    renderer.AddActor(actor)

#_create_path_geometry(renderer, path)

## Create a PathGroup from an SV file.
#
home = str(Path.home())
file_name = home+"/Simvascular/DemoProject/Paths/aorta.pth"
aorta_group = sv.path_group.read(file_name)
print("Number of paths: {0:d}".format(aorta_group.get_time_size()))
print("Method: {0:s}".format(aorta_group.get_method()))
print("Path at time 0:")
aorta_path = aorta_group.get_path(0)
control_points = aorta_path.get_control_points()
print("  Number of control points: {0:d}".format(len(control_points)))
curve_points = aorta_path.get_curve_points()
print("  Number of curve points: {0:d}".format(len(curve_points)))

## Create renderer and graphics window.
renderer = vtk.vtkRenderer()
renderer_win = vtk.vtkRenderWindow()
renderer_win.AddRenderer(renderer)
renderer.SetBackground(0.8, 0.8, 0.8)
renderer_win.SetSize(500, 500)
renderer_win.Render()
renderer_win.SetWindowName("Vis Path")

## Create path geometry.
create_path_geometry(renderer, aorta_path)

## Create a trackball interacter to transoform the geometry using the mouse.
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
interactor.SetRenderWindow(renderer_win)
interactor.Start()


