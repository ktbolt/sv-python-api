import sv 

#print(dir(path))

## create a Path .
#
cpt1 = [2.0, 0.0, 0.0] 
cpt2 = [3.0, 0.0, 0.0] 
cpt3 = [4.0, 0.0, 0.0] 
cpt4 = [5.0, 0.0, 0.0] 
path = sv.path.Path()
path.add_control_point(cpt1)
path.add_control_point(cpt2)
path.add_control_point(cpt3)
path.add_control_point(cpt4)

pt = path.get_point(2)
print(pt)

