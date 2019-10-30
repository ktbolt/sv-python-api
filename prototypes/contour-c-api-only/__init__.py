
import ctypes
import sys

## Set the shared library extension.
#
if sys.platform == "darwin":
    ext = "dylib"
elif sys.platform == "linux2":
    ext = "so"
elif sys.platform == "win32" or sys.platform =="cygwin":
    ext = "dll"

contour_lib = ctypes.PyDLL('libcontour.' + ext)
init_contour = contour_lib.PyInit_contour_module 
init_contour.restype = ctypes.py_object
contour = init_contour()

