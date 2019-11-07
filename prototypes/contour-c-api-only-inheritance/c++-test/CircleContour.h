
#ifndef SV3_CIRCLE_CONTOUR_H
#define SV3_CIRCLE_CONTOUR_H

#include "Contour.h"

#include <array>
#include <vector>

class CircleContour : public Contour { 

  public:
    CircleContour() {};
    ~CircleContour();
    void SetRadius(double radius);

    double m_Radius; 

};


#endif
