
#include "Path.h"
#include <iostream>

Path::~Path()
{
  std::cout << "[Path::~Path] Path dtor" << std::endl;
}

void 
Path::AddControlPoint(std::array<double,3> point)
{
  m_ControlPoints.push_back(point);
}

std::string Path::GetClassName()
{
  return std::string("Path");
}


