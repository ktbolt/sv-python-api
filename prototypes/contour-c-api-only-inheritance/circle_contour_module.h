
// CircleContour module. 
//
#include <iostream>
#include <math.h>
#include <string>

#include "contour_module.h"
#include "path_module.h"
#include "CircleContour.h"

//---------------------
// CircleContourObject
//---------------------
// Define the CircleContour class (type).
//
typedef struct {
  ContourObject super;
  double radius;
} CircleContourObject;

//////////////////////////////////////////////////////
//          M o d u l e  F u n c t i o n s          //
//////////////////////////////////////////////////////
//
// Python API functions. 

//--------------------------
// CircleContour_set_radius 
//--------------------------
//
static PyObject*
CircleContour_set_radius(CircleContourObject* self, PyObject* args)
{
  double radius = 0.0;
 
  if (!PyArg_ParseTuple(args, "d", &radius)) {
      return nullptr;
  }
  auto pmsg = "[CircleContour::set_radius] ";
  std::cout << pmsg << "Set radius ..." << std::endl;
  std::cout << pmsg << "Radius: " << radius << std::endl;
  auto contour = dynamic_cast<CircleContour*>(self->super.contour);
  contour->SetRadius(radius);

  Py_RETURN_NONE;
}

//------------------------------------
// CircleContour_set_center_from_path
//------------------------------------
//
static PyObject*
CircleContour_set_center_from_path(CircleContourObject* self, PyObject* args)
{
  PyObject* pathArg;
  int pathIndex;

  if (!PyArg_ParseTuple(args, "Oi", &pathArg, &pathIndex)) {
      return nullptr;
  }
  auto pmsg = "[CircleContour::set_center_from_path] ";
  std::cout << pmsg << std::endl;
  std::cout << pmsg << "Set center from path ..." << std::endl;
  std::cout << pmsg << "Path index:" << pathIndex << std::endl;
  std::cout << pmsg << "Object type: " << pathArg->ob_type->tp_name << std::endl;
  //std::cout << pmsg << "PathType: " << pathArg->ob_type->tp_name << std::endl;

  /*
  #define PyObject_TypeCheck(ob, tp) \
    (Py_TYPE(ob) == (tp) || PyType_IsSubtype(Py_TYPE(ob), (tp)))

  #define Py_TYPE(ob)             (_PyObject_CAST(ob)->ob_type)
  */

  //std::cout << "PathType: " << &PathType << std::endl;
  //std::cout << "pathArg->ob_type: " << pathArg->ob_type << std::endl;

/*
  if (Py_TYPE(pathArg) == (&PathType)) {
      std::cout << pmsg << "OK: The 'path' argument is a Path object." << std::endl;
  }

*/
  if (!PyObject_TypeCheck(pathArg, &PathType)) {
      std::cout << pmsg << "ERROR: The 'path' argument is not a Path object." << std::endl;
      return nullptr;
  } 

  auto pathObj = (PathObject*)pathArg;
  auto path = pathObj->path; 
  int numControlPoints = path->m_ControlPoints.size();
  std::cout << "Path number of control points: " << numControlPoints << std::endl;


  Py_RETURN_NONE;
}

////////////////////////////////////////////////////////
//          M o d u l e  D e f i n i t i o n          //
////////////////////////////////////////////////////////

//-------------------------
// CircleContourObjectInit 
//-------------------------
// This is the __init__() method for the Contour class. 
//
// This function is used to initialize an object after it is created.
//
static int 
CircleContourObjectInit(CircleContourObject* self, PyObject* args, PyObject *kwds)
{ 
  static int numObjs = 1;
  std::cout << "[CircleContourObjectInit] New CircleContour object: " << numObjs << std::endl;
  self->super.count = numObjs;
  self->super.contour = new CircleContour();
  numObjs += 1;
  return 0;
}

static PyMethodDef CircleContourMethods[] = {
  { "set_center_from_path", (PyCFunction)CircleContour_set_center_from_path, METH_VARARGS, NULL},
  { "set_radius", (PyCFunction)CircleContour_set_radius, METH_VARARGS, NULL},
  {NULL,NULL}
};

//------------------------
// CircleContourObjectNew 
//------------------------
//
static PyObject *
CircleContourObjectNew(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
  std::cout << "[CircleContourObjectNew] CircleContourObjectNew " << std::endl;
  auto self = (CircleContourObject*)type->tp_alloc(type, 0);
  if (self != NULL) {
      self->super.id = 2;
  }

  return (PyObject *) self;
}

//----------------------------
// CircleContourObjectDealloc 
//----------------------------
//
static void
CircleContourObjectDealloc(CircleContourObject* self)
{
  std::cout << "[CircleContourObjectDealloc] Free CircleContourObject" << std::endl;
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
static PyTypeObject CircleContourType = {
  PyVarObject_HEAD_INIT(NULL, 0)
  // Dotted name that includes both the module name and 
  // the name of the type within the module.
  .tp_name = "contour.CircleContour",
  .tp_basicsize = sizeof(CircleContourObject)
};

//----------------------------
// SetCircleContourTypeFields
//----------------------------
// Set the Python type object fields that stores Contour data. 
//
// Need to set the fields here because g++ does not suppor non-trivial 
// designated initializers. 
//
static void
SetCircleContourTypeFields(PyTypeObject& contourType)
 {
  // Doc string for this type.
  contourType.tp_doc = "CircleContour  objects";

  // Object creation function, equivalent to the Python __new__() method. 
  // The generic handler creates a new instance using the tp_alloc field.
  contourType.tp_new = CircleContourObjectNew;
  //.tp_new = PyType_GenericNew,

  contourType.tp_base = &ContourType;

  contourType.tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE;
  contourType.tp_init = (initproc)CircleContourObjectInit;
  contourType.tp_dealloc = (destructor)CircleContourObjectDealloc;
  contourType.tp_methods = CircleContourMethods;
};


