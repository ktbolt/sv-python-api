'''
Utilities. 
'''
import sv
import sys
import vtk

def setup_mesher(kernel):

    if kernel == sv.meshing.Kernel.TETGEN:
        mesher = sv.meshing.TetGen()
        # Load a model.
        file_name = '/Users/parkerda/SimVascular/DemoProject/Models/demo.vtp'
        file_name = 'cylinder-model.vtp'
        print("[setup_mesher] Model file name: {0:s}".format(file_name))
        mesher.load_model(file_name)

    return mesher

