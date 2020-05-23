''' This scipt tests writing a SV Model .mdl file.
'''
from pathlib import Path
import sv
import sys
import vtk
sys.path.insert(1, '../graphics/')
import graphics as gr

## Read an SV model group file. 
#
home = str(Path.home())
file_name = home + "/SimVascular/DemoProject/Models/cascade-model.mdl"
file_name = home + "/SimVascular/DemoProject/Models/parasolid-model.mdl"
file_name = home + "/SimVascular/DemoProject/Models/demo.mdl"
print("Read SV mdl file: {0:s}".format(file_name))
group = sv.modeling.Group(file_name)
num_models = group.get_num_models()
print("  Number of models: {0:d}".format(num_models))

## Write group.
file_name = "group-write-test.mdl"
group.write(file_name)

