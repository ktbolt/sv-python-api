
// Prototype using only the C API to implement a Path module. 
//

#include <iostream>
#include <map>
#include <math.h>
#include <string>

#include "Path.h"

#include "path_module.h"

#include <Python.h>

// Exception type used by PyErr_SetString() to set the for the error indicator.
static PyObject * PyRunTimeErrPg;

//////////////////////////////////////////////////////
//          M o d u l e  F u n c t i o n s          //
//////////////////////////////////////////////////////
//
// Python API functions. 

//------------------------
// Path_add_control_point
//------------------------
//
static PyObject*
Path_add_control_point(PathObject* self, PyObject* args)
{
  auto pmsg = "[Path_add_control_point] ";
  std::cout << pmsg << std::endl;
  std::cout << pmsg << "Add control point ..." << std::endl;

  PyObject *pointArg = nullptr;

  if (!PyArg_ParseTuple(args, "O", &pointArg)) {
      return nullptr;
  }

  std::cout << pmsg << "Id: " << self->id << std::endl;

  // Get the point.
  //
  std::array<double,3> point;
  for (int i = 0; i < 3; i++) {
      point[i] = PyFloat_AsDouble(PyList_GetItem(pointArg,i));
  }
  std::cout << pmsg << "  Point: " << point[0] << "  " << point[1] << "  " << point[2] << std::endl;

  if (self->path == nullptr) {
      PyErr_SetString(PyRunTimeErrPg, "Path object is null.");
      return nullptr;
  }

  auto path = self->path;
  path->AddControlPoint(point);
  std::cout << pmsg << "Class name: " << path->GetClassName() << std::endl;

  Py_RETURN_NONE;
}

//-------------------
// Path_get_geometry 
//--------------------
// Get the VTK polydata lines for the path 
// control points.
//
static PyObject*
Path_get_geometry(PathObject* self, PyObject* args)
{
  auto pmsg = "[Path_get_geometry] ";
  std::cout << pmsg << std::endl;
  std::cout << pmsg << "Get control points geometry ..." << std::endl;
  PyObject *vtkArg = nullptr;

  /*
  if (!PyArg_ParseTuple(args, "O", &vtkArg)) {
      return nullptr;
  }
  */

  Py_RETURN_NONE;
}

////////////////////////////////////////////////////////
//          M o d u l e  D e f i n i t i o n          //
////////////////////////////////////////////////////////

static const char* MODULE_NAME = "path";
static const char* MODULE_CONTOUR_CLASS = "Path";
static const char* MODULE_EXCEPTION = "path.PathError";
static const char* MODULE_EXCEPTION_OBJECT = "PathError";

PyDoc_STRVAR(module_doc, "path_module module functions.");

//------------------------------------
// Define the PathType type object
//------------------------------------
// Define the Python type object that stores Path data. 
//
// Can't set all the fields here because g++ does not suppor non-trivial 
// designated initializers. 
//
PyTypeObject PathType =
{
  PyVarObject_HEAD_INIT(NULL, 0)
  // Dotted name that includes both the module name and 
  // the name of the type within the module.
  .tp_name = "path.Path",
  .tp_basicsize = sizeof(PathObject)
};

//----------------
// PathObjectInit
//----------------
// This is the __init__() method for the Path class. 
//
// This function is used to initialize an object after it is created.
//
static int 
PathObjectInit(PathObject* self, PyObject* args, PyObject *kwds)
{
  static int numObjs = 1;
  std::cout << "[PathObjectInit] New Path object: " << numObjs << std::endl;

  self->count = numObjs;
  self->path = new Path();
  numObjs += 1;
  return 0;
}

//-------------
// PathMethods
//-------------
//
static PyMethodDef PathMethods[] = {
  { "add_control_point", (PyCFunction)Path_add_control_point, METH_VARARGS, NULL},
  { "get_geometry", (PyCFunction)Path_get_geometry, METH_VARARGS, NULL},
  {NULL,NULL}
};

//---------------
// PathObjectNew
//---------------
//
static PyObject * 
PathObjectNew(PyTypeObject *type, PyObject *args, PyObject *kwds)
{   
  std::cout << "[PathObjectNew] PathObjectNew " << std::endl;
  auto self = (PathObject*)type->tp_alloc(type, 0);
  if (self != NULL) {
      self->id = 1;
  }

  return (PyObject *) self;
}

//------------------
// PathObjectDelete
//------------------
//
static void 
PathObjectDealloc(PathObject* self)
{
  std::cout << "[PathObjectDealloc] Free PathObject" << std::endl;
  delete self->path;
  Py_TYPE(self)->tp_free(self);
}

//-------------------
// SetPathTypeFields 
//-------------------
// Set the Python type object fields that stores Path data. 
//
// Need to set the fields here because g++ does not suppor non-trivial 
// designated initializers. 
//
static void
SetPathTypeFields(PyTypeObject& contourType)
{
  // Doc string for this type.
  contourType.tp_doc = "Path  objects";
  // Object creation function, equivalent to the Python __new__() method. 
  // The generic handler creates a new instance using the tp_alloc field.
  contourType.tp_new = PathObjectNew;
  //contourType.tp_new = PyType_GenericNew,
  contourType.tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE;
  contourType.tp_init = (initproc)PathObjectInit;
  contourType.tp_dealloc = (destructor)PathObjectDealloc;
  contourType.tp_methods = PathMethods;
};

//----------------
// Module methods
//----------------
//
static PyMethodDef PathModuleMethods[] =
{
  {NULL, NULL, 0, NULL}
};

//---------------
// CreatePath
//---------------
// 
PyObject * 
CreatePath()
{
  auto * path = PyObject_CallObject((PyObject*)&PathType, NULL);
  return path; 
}

//---------------------------------------------------------------------------
//                           PYTHON_MAJOR_VERSION 3                         
//---------------------------------------------------------------------------

#if PY_MAJOR_VERSION >= 3

//---------------------
// Module definitation
//---------------------
//
static struct PyModuleDef PathModule =
{
    PyModuleDef_HEAD_INIT,
    MODULE_NAME, 
    module_doc,
    -1,
   PathModuleMethods 
};

//----------------
// PyInit_contour
//----------------
// The initialization function called by the Python interpreter 
// when the module is loaded.
//
// The name of this function needs to be PyInit_MODULE_NAME
//
PyMODINIT_FUNC
PyInit_path(void)
{
  std::cout << "Load path module." << std::endl;

  // Setup the Path object type.
  //
  SetPathTypeFields(PathType);
  if (PyType_Ready(&PathType) < 0) {
      std::cout << "Error creating Path type" << std::endl;
      return nullptr;
  }

  // Create the path module.
  auto module = PyModule_Create(&PathModule);
  if (module == NULL) {
      std::cout << "Error in initializing path" << std::endl;
      return nullptr;
  }

  // Add contour.PathException exception.
  /*
  PyRunTimeErr = PyErr_NewException(MODULE_EXCEPTION, NULL, NULL);
  PyModule_AddObject(module, MODULE_EXCEPTION_OBJECT, PyRunTimeErr);
  */

  // Add the 'Path' object.
  Py_INCREF(&PathType);
  PyModule_AddObject(module, MODULE_CONTOUR_CLASS, (PyObject*)&PathType);

  return module;
}

#endif
