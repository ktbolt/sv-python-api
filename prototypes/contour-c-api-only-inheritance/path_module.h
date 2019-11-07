
// Prototype using only the C API to implement a Contour module. 
//

#ifndef SV3_PATH_MODULE_H
#define SV3_PATH_MODULE_H

#include "Path.h"
#include <Python.h>

#include <iostream>
#include <math.h>
#include <string>

//------------
// PathObject
//------------
// Define the Path class (type).
//
typedef struct {
  PyObject_HEAD
  Path* path;
  int count;
  int id;
} PathObject;

//------------------------------------
// Define the PathType type object
//------------------------------------
// Define the Python type object that stores Path data. 
//
// Can't set all the fields here because g++ does not suppor non-trivial 
// designated initializers. 
//
static PyTypeObject PathType =
{
  PyVarObject_HEAD_INIT(NULL, 0)
  // Dotted name that includes both the module name and 
  // the name of the type within the module.
  .tp_name = "path.Path",
  .tp_basicsize = sizeof(PathObject)
};


#endif

