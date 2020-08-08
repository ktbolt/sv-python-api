''' Test the Model class. 
'''
import sv
import sys
import vtk
sys.path.insert(1, '../graphics/')
import graphics as gr

# Create a modeler.
modeler = sv.modeling.Modeler(sv.modeling.Kernel.POLYDATA)
print("Modeler type: " + str(type(modeler)))
print("Modeler kernel: " + str(modeler.kernel))

## The Model class is not exposed.
print("\n\n")
model = sv.modeling.Model(sv.modeling.Kernel.POLYDATA)
print("Model type: " + str(type(model)))
print("\n\n")

