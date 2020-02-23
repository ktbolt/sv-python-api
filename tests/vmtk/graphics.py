import sv
import vtk
from math import sqrt

def add_sphere(renderer, center, radius, color=[1.0, 1.0, 1.0], wire=False):
    sphere = vtk.vtkSphereSource()
    sphere.SetCenter(center[0], center[1], center[2])
    sphere.SetRadius(radius) 
    sphere.SetPhiResolution(16)
    sphere.SetThetaResolution(16)
    sphere.Update()
    sphere_pd = sphere.GetOutput() 
    add_geom(renderer, sphere_pd, color, wire)

class MouseInteractorStyle(vtk.vtkInteractorStyleTrackballCamera):

    def __init__(self):
        #self.AddObserver("LeftButtonPressEvent", self.leftButtonPressEvent)
        self.AddObserver("KeyPressEvent", self.onKeyPressEvent)
        self.AddObserver("CharEvent", self.onCharEvent)
        self.selected_points = []
        self.polydata = None
        self.data_name = None

    def leftButtonPressEvent(self, obj, event):
        """ 
        Process left mouse button press.
        """
        clickPos = self.GetInteractor().GetEventPosition()
        picker = vtk.vtkCellPicker()
        picker.Pick(clickPos[0], clickPos[1], 0, self.renderer)

        position = picker.GetPickPosition()
        cell_id = picker.GetCellId()

        if cell_id == -1: 
            return

        print(" ")
        print("Picked position: {0:g} {1:g} {2:g} ".format(position[0], position[1], position[2]))
        print("Cell id is: {0:d}".format(cell_id))

        min_i = -1
        min_d = 1e5
        min_p = []
        surface = self.polydata 
        points = surface.GetPoints()

        for i in range(points.GetNumberOfPoints()):
            p = 3*[0.0]
            points.GetPoint(i,p)
            dx = p[0] - position[0]
            dy = p[1] - position[1]
            dz = p[2] - position[2]
            d = sqrt(dx*dx + dy*dy + dz*dz)
            if d < min_d:
                min_d = d
                min_p = p
                min_i = i

        print("Picked node: {0:d} {1:g} {2:g} {3:g} ".format(min_i, min_p[0], min_p[1], min_p[2]))
        add_sphere(self.renderer, min_p, 0.1, color=[1.0, 1.0, 1.0], wire=False)

        cell_data = self.polydata.GetCellData().GetArray(self.data_name)
        print("Data name: {0:s}".format(self.data_name))
        value = cell_data.GetValue(cell_id)
        print("ID: {0:d}".format(value))

        #self.OnLeftButtonDown()
        return

    def onCharEvent(self, renderer, event):
        """
        Process an on char event.

        This is used to prevent passing the shortcut key 'w' to vtk which we use
        to write selected results and vtk uses to switch to wireframe display. 
        """
        key = self.GetInteractor().GetKeySym()
        if (key != 'w'):
            self.OnChar()
  
    def onKeyPressEvent(self, renderer, event):
        """
        Process a key press event.
        """
        key = self.GetInteractor().GetKeySym()

        if (key == 's'):
            self.leftButtonPressEvent(None, event)
        elif (key == 'f'):
            self.fix()

def display(renderer, renderer_win, polydata, data_name):
    interactor = vtk.vtkRenderWindowInteractor()

    # Add the custom style.
    style = MouseInteractorStyle()
    style.renderer = renderer
    style.polydata = polydata 
    style.data_name = data_name 
    style.SetCurrentRenderer(renderer)

    interactor.SetInteractorStyle(style)
    interactor.SetRenderWindow(renderer_win)
    interactor.Start()

def add_geom(renderer, polydata, color=[1.0, 1.0, 1.0], wire=False, line_width=1.0):
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(polydata)
    mapper.SetScalarVisibility(False)
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(color[0], color[1], color[2])
    actor.GetProperty().SetPointSize(5)
    actor.GetProperty().SetEdgeColor(0.0, 0.0, 0.0)
    actor.GetProperty().EdgeVisibilityOn()
    actor.GetProperty().SetOpacity(0.5)
    if wire:
        actor.GetProperty().SetRepresentationToWireframe()
    actor.GetProperty().SetLineWidth(line_width)
    renderer.AddActor(actor)

def init_graphics(win_width, win_height):
    '''
    Create renderer and graphics window.
    '''
    renderer = vtk.vtkRenderer()
    renderer_win = vtk.vtkRenderWindow()
    renderer_win.AddRenderer(renderer)
    renderer.SetBackground(0.8, 0.8, 0.8)
    renderer_win.SetSize(win_width, win_height)
    renderer_win.Render()
    renderer_win.SetWindowName("SV Vmtk Module")
    return renderer, renderer_win 


