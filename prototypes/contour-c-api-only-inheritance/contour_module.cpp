
// Prototype using only the C API to implement a Contour module. 
//

#include <iostream>
#include <map>
#include <math.h>
#include <string>

#include "Contour.h"
#include "CircleContour.h"

#include "contour_module.h"
#include "contour_module_kernel.h"

#include <Python.h>

// Exception type used by PyErr_SetString() to set the for the error indicator.
static PyObject * PyRunTimeErrPg;

PyObject * CreateContour(std::string kernelName);

//////////////////////////////////////////////////////
//          M o d u l e  F u n c t i o n s          //
//////////////////////////////////////////////////////
//
// Python API functions. 

//----------------
// Contour_create 
//----------------
//
static PyObject * 
Contour_create(PyObject* self, PyObject* args)
{
  char* kernelName = nullptr;

  if (!PyArg_ParseTuple(args, "s", &kernelName)) {
        return NULL;
  }

  std::cout << "[Contour_create] Kernel name: " << kernelName << std::endl;
  auto cont = CreateContour(std::string(kernelName));
  Py_INCREF(cont);
  return cont; 
}

//---------------------------
// Contour_add_control_point
//---------------------------
//
static PyObject*
Contour_add_control_point(ContourObject* self, PyObject* args)
{
  auto pmsg = "[Contour_add_control_point] ";
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

  if (self->contour == nullptr) {
      PyErr_SetString(PyRunTimeErrPg, "Contour object is null.");
      return nullptr;
  }

  auto contour = self->contour;
  contour->AddControlPoint(point);
  std::cout << pmsg << "Class name: " << contour->GetClassName() << std::endl;

  Py_RETURN_NONE;
}

//--------------------
// Contour_set_center 
//--------------------
//
static PyObject*
Contour_set_center(ContourObject* self, PyObject* args)
{
  auto pmsg = "[Contour_set_center] ";
  std::cout << pmsg << std::endl;
  std::cout << pmsg << "Set center ..." << std::endl;

  PyObject *centerArg = nullptr;

  if (!PyArg_ParseTuple(args, "O", &centerArg)) {
      return nullptr;
  }

  std::cout << pmsg << "Id: " << self->id << std::endl;

  // Get the center.
  //
  std::array<double,3> center;
  for (int i = 0; i < 3; i++) {
      center[i] = PyFloat_AsDouble(PyList_GetItem(centerArg,i));
  }
  std::cout << pmsg << "  Center: " << center[0] << "  " << center[1] << "  " << center[2] << std::endl;

  if (self->contour == nullptr) {
      PyErr_SetString(PyRunTimeErrPg, "Contour object is null.");
      return nullptr;
  }

  auto contour = self->contour;
  contour->SetCenter(center);
  std::cout << pmsg << "Class name: " << contour->GetClassName() << std::endl;

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

// Derived class names.
static const char* MODULE_CIRCLE_CONTOUR_CLASS = "CircleContour";
static const char* MODULE_POLYGON_CONTOUR_CLASS = "PolygonContour";

//-------------------
// ContourObjectInit
//-------------------
// This is the __init__() method for the Contour class. 
//
// This function is used to initialize an object after it is created.
//
static int 
ContourObjectInit(ContourObject* self, PyObject* args, PyObject *kwds)
{
  static int numObjs = 1;
  std::cout << "[ContourObjectInit] New Contour object: " << numObjs << std::endl;

  char* kernalName = nullptr;
  
  if (!PyArg_ParseTuple(args, "s", &kernalName)) {
      return -1;
  }

  std::cout << "[ContourObjectInit] Kernel name: " << kernalName << std::endl;

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
  { "set_center", (PyCFunction)Contour_set_center, METH_VARARGS, NULL},
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
  std::cout << "[ContourObjectDealloc] Free ContourObject" << std::endl;
  delete self->contour;
  Py_TYPE(self)->tp_free(self);
}

//----------------------
// SetContourTypeFields 
//----------------------
// Set the Python type object fields that stores Contour data. 
//
// Need to set the fields here because g++ does not suppor non-trivial 
// designated initializers. 
//
static void
SetContourTypeFields(PyTypeObject& contourType)
{
  // Doc string for this type.
  contourType.tp_doc = "Contour  objects";
  // Object creation function, equivalent to the Python __new__() method. 
  // The generic handler creates a new instance using the tp_alloc field.
  contourType.tp_new = ContourObjectNew;
  //contourType.tp_new = PyType_GenericNew,
  contourType.tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE;
  contourType.tp_init = (initproc)ContourObjectInit;
  contourType.tp_dealloc = (destructor)ContourObjectDealloc;
  contourType.tp_methods = ContourMethods;
};

//----------------
// Module methods
//----------------
//
static PyMethodDef ContourModuleMethods[] =
{
  {"create", Contour_create, METH_VARARGS, "Create a Contour object."},
  {NULL, NULL, 0, NULL}
};

// Include derived Contour classes.
#include "circle_contour_module.h"
#include "polygon_contour_module.h"

//---------------
// CreateContour
//---------------
// 
PyObject * 
CreateContour(std::string kernelName)
{
  auto * cont = PyObject_CallObject((PyObject*)&CircleContourType, NULL);
  return cont; 
}

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
  SetContourTypeFields(ContourType);
  if (PyType_Ready(&ContourType) < 0) {
      std::cout << "Error creating Contour type" << std::endl;
      return nullptr;
  }

  SetCircleContourTypeFields(CircleContourType);
  if (PyType_Ready(&CircleContourType) < 0) {
      std::cout << "Error creating CircleContour type" << std::endl;
      return nullptr;
  }

  SetPolygonContourTypeFields(PolygonContourType);
  if (PyType_Ready(&PolygonContourType) < 0) {
      std::cout << "Error creating PolygonContourType type" << std::endl;
      return nullptr;
  }

  SetContourKernelTypeFields(ContourKernelType);
  if (PyType_Ready(&ContourKernelType) < 0) {
      std::cout << "Error creating ContourKernel type" << std::endl;
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

  // Add the 'CircleContour' object.
  Py_INCREF(&CircleContourType);
  PyModule_AddObject(module, MODULE_CIRCLE_CONTOUR_CLASS, (PyObject*)&CircleContourType);

  // Add the 'PolygonContour' object.
  Py_INCREF(&PolygonContourType);
  PyModule_AddObject(module, MODULE_POLYGON_CONTOUR_CLASS, (PyObject*)&PolygonContourType);

  // Add the 'kernel' object.
  Py_INCREF(&ContourKernelType);
  PyModule_AddObject(module, "kernel", (PyObject*)&ContourKernelType);

  SetContourKernelTypes(ContourKernelType);

  return module;
}

#endif
