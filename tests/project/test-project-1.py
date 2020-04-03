'''
This script tests opening an SV project.
'''

from pathlib import Path
import project 

# Open a project.
home = str(Path.home())
project_path = home + "/Simvascular/DemoProject"
project = project.Project()
project.open(project_path)

# Print the plugins defined for the project.
print("Plugins: ") 
plugin_instances = project.get_project_plugin_instances()
for name, inst in plugin_instances.items(): 
    print("  {0:s} : {1:s}".format(name, inst))

# Get a SV path object.
right_iliac_path = project.get_path("right_iliac")

