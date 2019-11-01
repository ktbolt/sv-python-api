
#ifndef SV3_CONTOUR_H
#define SV3_CONTOUR_H

#include <array>
#include <vector>


enum cKernelType {
    cKERNEL_INVALID,
    cKERNEL_LEVELSET,
    cKERNEL_THRESHOLD,
    cKERNEL_CIRCLE,
    cKERNEL_POLYGON,
    cKERNEL_SPLINEPOLYGON,
    cKERNEL_ELLIPSE
};

class Contour { 

  public:
    Contour() {};
    ~Contour();

    void AddControlPoint(std::array<double,3> point);
    virtual std::string GetClassName();
    void SetCenter(std::array<double,3> center);

    std::array<double,3> m_Center;
    std::vector<std::array<double,3> > m_ControlPoints;
    std::vector<std::array<double,3> > m_ContourPoints;

};


#endif
