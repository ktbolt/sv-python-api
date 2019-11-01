
// Prototype using only the C API to implement a Contour module. 
//

#include <iostream>
#include <math.h>
#include <string>

#include "Contour.h"
#include <Python.h>

//---------------
// ContourObject
//---------------
// Define the Contour class (type).
//
typedef struct {
  PyObject_HEAD
  Contour* contour;
  int count;
  int id;
} ContourObject;

//////////////////////////////////////////////////////
//          M o d u l e  F u n c t i o n s          //
//////////////////////////////////////////////////////
//
// Python API functions. 

//----------
// cos_func 
//----------
//
static PyObject * 
cos_func(PyObject* self, PyObject* args)
{
    double value;
    double answer;

    if (!PyArg_ParseTuple(args, "d", &value)) {
        return NULL;
    }

    answer = cos(value);

    return Py_BuildValue("f", answer);
}

//---------------------------
// Contour_add_control_point
//---------------------------
//
static PyObject*
Contour_add_control_point(ContourObject* self, PyObject* args)
{
  auto pmsg = "[Contour::add_control_point] ";
  std::cout << pmsg << "Add control point ..." << std::endl;

  PyObject *pointArg = nullptr;

  if (!PyArg_ParseTuple(args, "O", &pointArg)) {
      return nullptr;
  }

  // Get the point.
  //
  std::array<double,3> point;
  for (int i = 0; i < 3; i++) {
      point[i] = PyFloat_AsDouble(PyList_GetItem(pointArg,i));
  }
  std::cout << pmsg << "  Point: " << point[0] << "  " << point[1] << "  " << point[2] << std::endl;

  auto contour = self->contour;
  contour->AddControlPoint(point);

  Py_RETURN_NONE;
}

////////////////////////////////////////////////////////
//          M o d u l e  D e f i n i t i o n          //
////////////////////////////////////////////////////////

static const char* MODULE_NAME = "contour";
static const char* MODULE_CONTOUR_CLASS = "Contour";
static const char* MODULE_EXCEPTION = "contour.ContourError";
static const char* MODULE_EXCEPTION_OBJECT = "ContourError";

PyDoc_STRVAR(module_doc, "contour_module module functions.");

//-------------------
// ContourObjectInit
//-------------------
// This is the __init__() method for the Contour class. 
//
// This function is used to initialize an object after it is created.
//
static int ContourObjectInit(ContourObject* self, PyObject* args, PyObject *kwds)
{
  static int numObjs = 1;
  std::cout << "[ContourObjectInit] New Contour object: " << numObjs << std::endl;
  self->count = numObjs;
  self->contour = new Contour();
  numObjs += 1;
  return 0;
}

//----------------
// ContourMethods
//----------------
//
static PyMethodDef ContourMethods[] = {
  { "add_control_point", (PyCFunction)Contour_add_control_point, METH_VARARGS, NULL},
  {NULL,NULL}
};

//------------------
// ContourObjectNew
//------------------
//
static PyObject * 
ContourObjectNew(PyTypeObject *type, PyObject *args, PyObject *kwds)
{   
  std::cout << "[ContourObjectNew] ContourObjectNew " << std::endl;
  auto self = (ContourObject*)type->tp_alloc(type, 0);
  if (self != NULL) {
      self->id = 1;
  }

  return (PyObject *) self;
}

//---------------------
// ContourObjectDelete
//---------------------
//
static void 
ContourObjectDealloc(ContourObject* self)
{
    delete self->contour;
    Py_TYPE(self)->tp_free(self);
}

//------------------------------------
// Define the ContourType type object
//------------------------------------
// Define the Python type object that stores Contour data. 
//
// Only set the fields we need, the remaining fields will be filled 
// with zeros by the compiler.
//
static PyTypeObject ContourType = {

  PyVarObject_HEAD_INIT(NULL, 0)

  // Dotted name that includes both the module name and 
  // the name of the type within the module.
  .tp_name = "contour.Contour",

  .tp_basicsize = sizeof(ContourObject),

  // Doc string for this type.
  .tp_doc = "Contour  objects", 

  // Object creation function, equivalent to the Python __new__() method. 
  // The generic handler creates a new instance using the tp_alloc field.
  .tp_new = ContourObjectNew,
  //.tp_new = PyType_GenericNew,

  .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
  .tp_init = (initproc)ContourObjectInit, 
  .tp_dealloc = (destructor)ContourObjectDealloc,
  .tp_methods = ContourMethods
};

//-------------------
// CreateContourType
//-------------------
// 
ContourObject * 
CreateContourType()
{
  return PyObject_New(ContourObject, &ContourType);
}

//----------------
// Module methods
//----------------
//
static PyMethodDef ContourModuleMethods[] =
{
    {"cos_func", cos_func, METH_VARARGS, "evaluate the cosine"},

   {NULL, NULL, 0, NULL}

};

//---------------------------------------------------------------------------
//                           PYTHON_MAJOR_VERSION 3                         
//---------------------------------------------------------------------------

#if PY_MAJOR_VERSION >= 3

//---------------------
// Module definitation
//---------------------
//
static struct PyModuleDef ContourModule =
{
    PyModuleDef_HEAD_INIT,
    MODULE_NAME, 
    module_doc,
    -1,
   ContourModuleMethods 
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
PyInit_contour(void)
{
  std::cout << "Load contour module." << std::endl;

  // Setup the Contour object type.
  //
  if (PyType_Ready(&ContourType) < 0) {
      std::cout << "Error creating Contour type" << std::endl;
      return nullptr;
  }

  // Create the contour module.
  auto module = PyModule_Create(&ContourModule);
  if (module == NULL) {
      std::cout << "Error in initializing pyContour" << std::endl;
      return nullptr;
  }

  // Add contour.ContourException exception.
  /*
  PyRunTimeErr = PyErr_NewException(MODULE_EXCEPTION, NULL, NULL);
  PyModule_AddObject(module, MODULE_EXCEPTION_OBJECT, PyRunTimeErr);
  */

  // Add the 'Contour' object.
  Py_INCREF(&ContourType);
  PyModule_AddObject(module, MODULE_CONTOUR_CLASS, (PyObject*)&ContourType);

  return module;
}

#endif
