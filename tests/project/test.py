'''
This script tests opening an SV project.
'''

import sv 

project_path = "/home/davep/Simvascular/DemoProject"

project = sv.project.Project()

project.open(project_path)

