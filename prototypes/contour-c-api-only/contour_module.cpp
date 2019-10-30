
// Prototype using only the C API to implement a Contour module. 
//

#include <iostream>
#include <math.h>
#include <string>

#include "Contour.h"
#include <Python.h>

typedef struct {
  PyObject_HEAD
  Contour* contour;
  int count;
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
static int ContourObjectInit(ContourObject* self, PyObject* args)
{
  static int numObjs = 1;
  std::cout << "New Contour object: " << numObjs << std::endl;
  self->count = numObjs;
  self->contour = new Contour();
  numObjs += 1;
  return 0;
}

static PyMethodDef ContourMethods[] = {

  { "add_control_point", (PyCFunction)Contour_add_control_point, METH_VARARGS, NULL},

};


//------------------------------------
// Define the ContourType type object
//------------------------------------
// The type object stores a large number of values, mostly C function pointers, 
// each of which implements a small part of the type’s functionality.
//
static PyTypeObject ContourType = {
  PyVarObject_HEAD_INIT(NULL, 0)
  "contour.Contour",         /* tp_name */
  sizeof(ContourObject),     /* tp_basicsize */
  0,                         /* tp_itemsize */
  0,                         /* tp_dealloc */
  0,                         /* tp_print */
  0,                         /* tp_getattr */
  0,                         /* tp_setattr */
  0,                         /* tp_compare */
  0,                         /* tp_repr */
  0,                         /* tp_as_number */
  0,                         /* tp_as_sequence */
  0,                         /* tp_as_mapping */
  0,                         /* tp_hash */
  0,                         /* tp_call */
  0,                         /* tp_str */
  0,                         /* tp_getattro */
  0,                         /* tp_setattro */
  0,                         /* tp_as_buffer */
  Py_TPFLAGS_DEFAULT |       /* tp_flags */
  Py_TPFLAGS_BASETYPE,   
  "Contour  objects",        /* tp_doc */
  0,                         /* tp_traverse */
  0,                         /* tp_clear */
  0,                         /* tp_richcompare */
  0,                         /* tp_weaklistoffset */
  0,                         /* tp_iter */
  0,                         /* tp_iternext */
  ContourMethods,            /* tp_methods */
  0,                         /* tp_members */
  0,                         /* tp_getset */
  0,                         /* tp_base */
  0,                         /* tp_dict */
  0,                         /* tp_descr_get */
  0,                         /* tp_descr_set */
  0,                         /* tp_dictoffset */
  (initproc)ContourObjectInit,  /* tp_init */
  0,                         /* tp_alloc */
  0,                         /* tp_new */
};

//-------------------
// createContourType
//-------------------
ContourObject * 
createContourType()
{
  return PyObject_New(ContourObject, &ContourType);
}

//----------------
// Module methods
//----------------
//
static PyMethodDef module_methods[] =
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
    module_methods
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

  // Create the Contour class type.
  ContourType.tp_new = PyType_GenericNew;
  if (PyType_Ready(&ContourType) < 0) {
      std::cout << "Error in pyContourType" << std::endl;
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
