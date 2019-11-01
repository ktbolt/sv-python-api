
// ContourKernel type. 
//
#include <iostream>
#include <math.h>
#include <string>
#include <structmember.h>

#include "contour_module.h"

//---------------------
// ContourKernelObject
//---------------------
// Define the ContourKernelObject class (type).
//
typedef struct {
  //const char* circle = "circle";
  PyObject* circle;
} ContourKernelObject;


//////////////////////////////////////////////////////
//          M o d u l e  F u n c t i o n s          //
//////////////////////////////////////////////////////
//
// Python API functions. 

////////////////////////////////////////////////////////
//          M o d u l e  D e f i n i t i o n          //
////////////////////////////////////////////////////////

//-------------------------
// ContourKernelObjectInit 
//-------------------------
// This is the __init__() method for the Contour class. 
//
// This function is used to initialize an object after it is created.
//
static int 
ContourKernelObjectInit(ContourKernelObject* self, PyObject* args, PyObject *kwds)
{ 
  //static int numObjs = 1;
  std::cout << "[ContourKernelObjectInit] New ContourKernel object: " << std::endl;
  //self->super.count = numObjs;
  //self->super.contour = new ContourKernel();
  //numObjs += 1;
  return 0;
}

static PyMethodDef ContourKernelMethods[] = {
  {NULL,NULL}
};

/*
static PyMemberDef ContourKernelMembers[] = 
{
  {"circle", T_OBJECT_EX, offsetof(ContourKernelObject, circle), 0, "circle kernel"},
  //{"circle", T_STRING, offsetof(ContourKernelObject, circle), 0, "circle kernel"},
  {NULL}
};
*/

static PyObject*
ContourKernelGetType(ContourKernelObject* self, void* closure)
{
    return PyUnicode_FromString("circle");
    //return self->circle;
}

static PyGetSetDef ContourKernelGetSets[] = 
{
  {"circle", (getter)ContourKernelGetType, NULL, NULL, NULL},
  {NULL}
};


//------------------------
// ContourKernelObjectNew 
//------------------------
//
static PyObject *
ContourKernelObjectNew(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
  std::cout << "[ContourKernelObjectNew] ContourKernelObjectNew " << std::endl;
  auto self = (ContourKernelObject*)type->tp_alloc(type, 0);
  if (self != NULL) {
      self->circle = PyUnicode_FromString("Circle");
  }

  return (PyObject *) self;
}

//----------------------------
// ContourKernelObjectDealloc 
//----------------------------
//
static void
ContourKernelObjectDealloc(ContourKernelObject* self)
{
  std::cout << "[ContourKernelObjectDealloc] Free ContourKernelObject" << std::endl;
  //delete self->super.contour;
  //Py_TYPE(self)->tp_free(self);
}

//------------------------------------
// Define the ContourType type object
//------------------------------------
// Define the Python type object that stores Contour data. 
//
// Can't set all the fields here because g++ does not suppor non-trivial 
// designated initializers. 
//
static PyTypeObject ContourKernelType = {
  PyVarObject_HEAD_INIT(NULL, 0)
  // Dotted name that includes both the module name and 
  // the name of the type within the module.
  .tp_name = "kernel",
  //.tp_name = "contour.kernel",
  .tp_basicsize = sizeof(ContourKernelObject)
};

//----------------------------
// SetContourKernelTypeFields
//----------------------------
// Set the Python type object fields that stores Contour data. 
//
// Need to set the fields here because g++ does not suppor non-trivial 
// designated initializers. 
//
static void
SetContourKernelTypeFields(PyTypeObject& contourType)
 {
  // Doc string for this type.
  contourType.tp_doc = "ContourKernel  objects";

  // Object creation function, equivalent to the Python __new__() method. 
  // The generic handler creates a new instance using the tp_alloc field.
  contourType.tp_new = ContourKernelObjectNew;
  //.tp_new = PyType_GenericNew,

  contourType.tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE;
  contourType.tp_init = (initproc)ContourKernelObjectInit;
  contourType.tp_dealloc = (destructor)ContourKernelObjectDealloc;
  contourType.tp_methods = ContourKernelMethods;
  contourType.tp_getset = ContourKernelGetSets;
  //contourType.tp_members = ContourKernelMembers;
};

#if PY_MAJOR_VERSION >= 3

//---------------------
// Module definitation
//---------------------
//
static struct PyModuleDef ContourKernelModule =
{
    PyModuleDef_HEAD_INIT,
    "contour.kernel", 
    "",
    -1,
    ContourKernelMethods 
};

//----------------
// PyInit_contour_kernel
//----------------
// The initialization function called by the Python interpreter 
// when the module is loaded.
//
// The name of this function needs to be PyInit_MODULE_NAME
//
PyMODINIT_FUNC
PyInit_contour_kernel(void)
{
  std::cout << "Load contour.kernel module." << std::endl;

  // Setup the Contour object type.
  //
  SetContourKernelTypeFields(ContourKernelType);
  if (PyType_Ready(&ContourKernelType) < 0) {
      std::cout << "Error creating ContourKernel type" << std::endl;
      return nullptr;
  }

  // Create the contour module.
  auto module = PyModule_Create(&ContourKernelModule);
  if (module == NULL) {
      std::cout << "Error in initializing ContourKernel" << std::endl;
      return nullptr;
  }

  // Add the 'kernel' object.
  Py_INCREF(&ContourKernelType);
  PyModule_AddObject(module, "kernel", (PyObject*)&ContourKernelType);

  return module;
}

#endif

