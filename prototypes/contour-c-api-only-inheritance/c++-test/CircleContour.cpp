
#include "CircleContour.h"
#include <iostream>

CircleContour::~CircleContour()
{
  std::cout << "[CircleContour::~CircleContour] CircleContour dtor" << std::endl;
}

void 
CircleContour::SetRadius(double radius)
{
  m_Radius = radius; 
}


