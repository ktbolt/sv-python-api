'''
Test solid.Modeler read methods. 
'''
import sv
import vtk
import sys
sys.path.insert(1, '../graphics/')
import graphics as gr

## Create a modeler.
modeler = sv.modeling.Modeler(sv.modeling.Kernel.OPENCASCADE)
modeler = sv.modeling.Modeler(sv.modeling.Kernel.POLYDATA)

## Read a model.
print("Read modeling model file ...")
file_name = "cylinder.brep"
file_name = "cylinder.stl"
model = modeler.read(file_name)
print("Model type: " + str(type(model)))
model_pd = model.get_polydata()

## Create renderer and graphics window.
win_width = 500
win_height = 500
renderer, renderer_window = gr.init_graphics(win_width, win_height)

## Add model polydata.
gr.add_geometry(renderer, model_pd, color=[0.0, 1.0, 0.0], wire=False, edges=False)

# Display window.
gr.display(renderer_window)

