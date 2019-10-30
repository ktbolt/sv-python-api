
#include "Contour.h"


void 
Contour::AddControlPoint(std::array<double,3> point)
{
  m_ControlPoints.push_back(point);
}


