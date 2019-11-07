
#include "Contour.h"
#include "CircleContour.h"

#include <iostream>

int main(int numArgs, char** args)
{
  std::cout << "Start " << std::endl;

  std::array<double,3> point {1.0, 0.0, 0.0};
  auto cont = new Contour();
  cont->AddControlPoint(point);
  delete cont;

  auto circleCont = new CircleContour();
  circleCont->AddControlPoint(point);
  delete circleCont;

}


