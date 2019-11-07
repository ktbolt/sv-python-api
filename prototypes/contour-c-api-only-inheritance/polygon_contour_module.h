
// CircleContour module. 
//
#include <iostream>
#include <math.h>
#include <string>

#include "contour_module.h"
#include "PolygonContour.h"

//---------------------
// PolygonContourObject
//---------------------
// Define the PolygonContour class (type).
//
typedef struct {
  ContourObject super;
} PolygonContourObject;

//////////////////////////////////////////////////////
//          M o d u l e  F u n c t i o n s          //
//////////////////////////////////////////////////////
//
// Python API functions. 

/*
static PyObject*
PolygonContour_set_radius(PolygonContourObject* self, PyObject* args)
{
  double radius = 0.0;
 
  if (!PyArg_ParseTuple(args, "d", &radius)) {
      return nullptr;
  }
  auto pmsg = "[PolygonContour::set_radius] ";
  std::cout << pmsg << "Set radius ..." << std::endl;
  std::cout << pmsg << "Radius: " << radius << std::endl;
  auto contour = dynamic_cast<PolygonContour*>(self->super.contour);
  contour->SetRadius(radius);

  Py_RETURN_NONE;
}
*/

////////////////////////////////////////////////////////
//          M o d u l e  D e f i n i t i o n          //
////////////////////////////////////////////////////////

//-------------------------
// PolygonContourObjectInit 
//-------------------------
// This is the __init__() method for the Contour class. 
//
// This function is used to initialize an object after it is created.
//
static int 
PolygonContourObjectInit(PolygonContourObject* self, PyObject* args, PyObject *kwds)
{ 
  static int numObjs = 1;
  std::cout << "[PolygonContourObjectInit] New PolygonContour object: " << numObjs << std::endl;
  self->super.count = numObjs;
  self->super.contour = new PolygonContour();
  numObjs += 1;
  return 0;
}

static PyMethodDef PolygonContourMethods[] = {
  {NULL,NULL}
};

//------------------------
// PolygonContourObjectNew 
//------------------------
//
static PyObject *
PolygonContourObjectNew(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
  std::cout << "[PolygonContourObjectNew] PolygonContourObjectNew " << std::endl;
  auto self = (PolygonContourObject*)type->tp_alloc(type, 0);
  if (self != NULL) {
      self->super.id = 3;
  }

  return (PyObject *) self;
}

//----------------------------
// PolygonContourObjectDealloc 
//----------------------------
//
static void
PolygonContourObjectDealloc(PolygonContourObject* self)
{
  std::cout << "[PolygonContourObjectDealloc] Free PolygonContourObject" << std::endl;
  delete self->super.contour;
  Py_TYPE(self)->tp_free(self);
}

//------------------------------------
// Define the ContourType type object
//------------------------------------
// Define the Python type object that stores Contour data. 
//
// Can't set all the fields here because g++ does not suppor non-trivial 
// designated initializers. 
//
static PyTypeObject PolygonContourType = {
  PyVarObject_HEAD_INIT(NULL, 0)
  // Dotted name that includes both the module name and 
  // the name of the type within the module.
  .tp_name = "contour.PolygonContour",
  .tp_basicsize = sizeof(PolygonContourObject)
};

//----------------------------
// SetPolygonContourTypeFields
//----------------------------
// Set the Python type object fields that stores Contour data. 
//
// Need to set the fields here because g++ does not suppor non-trivial 
// designated initializers. 
//
static void
SetPolygonContourTypeFields(PyTypeObject& contourType)
 {
  // Doc string for this type.
  contourType.tp_doc = "PolygonContour  objects";

  // Object creation function, equivalent to the Python __new__() method. 
  // The generic handler creates a new instance using the tp_alloc field.
  contourType.tp_new = PolygonContourObjectNew;
  //.tp_new = PyType_GenericNew,

  contourType.tp_base = &ContourType;

  contourType.tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE;
  contourType.tp_init = (initproc)PolygonContourObjectInit;
  contourType.tp_dealloc = (destructor)PolygonContourObjectDealloc;
  contourType.tp_methods = PolygonContourMethods;
};


