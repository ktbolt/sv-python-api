
// Prototype using only the C API to implement a Contour module. 
//

#ifndef SV3_CONTOUR_MODULE_H
#define SV3_CONTOUR_MODULE_H

#include "Contour.h"
#include <Python.h>

#include <iostream>
#include <math.h>
#include <string>

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

//------------------------------------
// Define the ContourType type object
//------------------------------------
// Define the Python type object that stores Contour data. 
//
// Can't set all the fields here because g++ does not suppor non-trivial 
// designated initializers. 
//
static PyTypeObject ContourType =
{
  PyVarObject_HEAD_INIT(NULL, 0)
  // Dotted name that includes both the module name and 
  // the name of the type within the module.
  .tp_name = "contour.Contour",
  .tp_basicsize = sizeof(ContourObject)
};


#endif

