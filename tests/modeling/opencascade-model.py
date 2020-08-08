'''Test creating an Open Cascade solid model.
'''
import sv
import sys
import vtk
sys.path.insert(1, '../graphics/')
import graphics as gr

## Create a model.
print("Create an sv.modeling.OpenCascade model directly.")
model = sv.modeling.OpenCascade()
print("Model type: ", str(type(model)))

## Read in a model.
#
# [TODO:Davep] Add 'read' method?
#
model.read("cylinder-opencascade.brep")

polydata = model.get_polydata() 




