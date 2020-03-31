'''
This script tests opening an SV project.
'''

from pathlib import Path
import sv 

home = str(Path.home())
project_path = home + "/Simvascular/DemoProject"
project = sv.project.Project()
project.open(project_path)

