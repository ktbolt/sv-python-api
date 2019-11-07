
#include "PolygonContour.h"
#include <iostream>

PolygonContour::~PolygonContour()
{
  std::cout << "[PolygonContour::~PolygonContour] PolygonContour dtor" << std::endl;
}

std::string PolygonContour::GetClassName()
{
  return std::string("PolygonContour");
}

