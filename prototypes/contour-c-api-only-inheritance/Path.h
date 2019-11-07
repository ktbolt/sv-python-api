
#ifndef SV3_PATH_H
#define SV3_PATH_H

#include <array>
#include <vector>


class Path { 

  public:
    Path() {};
    ~Path();

    void AddControlPoint(std::array<double,3> point);
    virtual std::string GetClassName();

    std::vector<std::array<double,3> > m_ControlPoints;
    std::vector<std::array<double,3> > m_PathPoints;

};


#endif
