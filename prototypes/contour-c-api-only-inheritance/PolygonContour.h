
#ifndef SV3_POLYGON_CONTOUR_H
#define SV3_POLYGON_CONTOUR_H

#include "Contour.h"

#include <array>
#include <vector>

class PolygonContour : public Contour { 

  public:
    PolygonContour() {};
    ~PolygonContour();

    std::string GetClassName();
};


#endif
