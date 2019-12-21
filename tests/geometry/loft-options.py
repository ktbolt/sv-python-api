'''
Test the sv.geometry.LoftOptions() class. 
'''
from pathlib import Path
import sv
import vtk

loft_options = sv.geometry.LoftOptions()
#loft_options = sv.geometry.LoftOptions(num_out_pts_in_segs=40)
print(dir(loft_options))

print("loft_options.num_out_pts_in_segs: " + str(loft_options.num_out_pts_in_segs))
print("loft_options.use_fft: " + str(loft_options.use_fft))

numOutPtsInSegs = 60
numOutPtsAlongLength = 12
numPtsInLinearSampleAlongLength = 240
numLinearPtsAlongLength = 120
numModes = 20
useFFT = 0
useLinearSampleAlongLength = 1


