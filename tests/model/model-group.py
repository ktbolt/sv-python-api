from pathlib import Path
import sv

#print(dir(sv))
#print(dir(sv.solid))

## Read an SV model group file. 
#
home = str(Path.home())
file_name = home + "/SimVascular/DemoProject/Models/aorta-small.mdl"
file_name = home + "/SimVascular/DemoProject/Models/parasolid-model.mdl"
file_name = home + "/SimVascular/DemoProject/Models/demo.mdl"
print("Read SV mdl file: {0:s}".format(file_name))
demo_models = sv.solid.Group(file_name)
num_models = demo_models.number_of_models()
print("Number of models: {0:d}".format(num_models))

model = demo_models.get_model(0)
print("Model type: " + str(type(model)))

 

