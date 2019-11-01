
#include "Contour.h"
#include <iostream>

Contour::~Contour()
{
  std::cout << "Contour dtor" << std::endl;
}

void 
Contour::AddControlPoint(std::array<double,3> point)
{
  m_ControlPoints.push_back(point);
}


