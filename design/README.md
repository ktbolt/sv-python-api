
 # SimVascular Python API Design 
 

The SV Python API provides an interface to SV objects and functions using Python.

# SV Classes

## Repository

**cvRepositoryData**
```
class SV_EXPORT_REPOSITORY cvRepositoryData {

  public:

  private:
      RepositoryDataT type_;
      char name_[RD_MAX_NAME_LEN];
      int lockCnt_;
      Tcl_HashTable labels_;

};
```

**cvDataObject**
```
class SV_EXPORT_REPOSITORY cvDataObject : public cvRepositoryData {

  public:
      cvDataObject( RepositoryDataT type );
      virtual ~cvDataObject();

      vtkDataObject *GetVtkPtr() { return data_; };
      virtual int GetMemoryUsage();

  protected:
      vtkDataObject *data_;

};
```

## Path

```
class SV_EXPORT_PATH PathElement : public cvRepositoryData

  public:
      std::vector<std::array<double,3> > GetControlPoints();

  protected:
      std::vector<svControlPoint> m_ControlPoints;
      std::vector<PathPoint> m_PathPoints;
      double m_Spacing;
      CalculationMethod m_Method;
      int m_CalculationNumber;
}
```

```
class SV_EXPORT_PATH PathGroup : public cvRepositoryData
{
  public:
      PathElement* GetPathElement(unsigned int t = 0) const;

  protected:

    std::vector< sv3::PathElement* > m_PathElementSet;
}

```

## Contour

There are four classes derived from the Contour base class

1) circleContour
2) levelSetContour
3) ContourPolygon
4) thresholdContour


**Contour**
```
class SV_EXPORT_SEGMENTATION Contour : public cvRepositoryData
{
  public:
    struct svLSParam { double ctrx; double ctry; double ctrz; ... }
      
    virtual std::string GetClassName();
    virtual void SetControlPoint(int index, std::array<double,3> point);
    virtual void PlaceControlPoints(std::array<double,3> point);
    virtual void SetControlPointByRadius(double radius, double* point){return;};
    virtual void CreateContourPoints(){return;};
    virtual void ContourPointsChanged();

    virtual void CreateCenterScalingPoints();
    virtual void AssignCenterScalingPoints();
    virtual Contour* CreateSmoothedContour(int fourierNumber = 12 );
    virtual int SearchControlPointByContourPoint( int contourPointIndex );
    virtual void SetLevelSetParas(svLSParam* paras){return;};

    virtual svLSParam* GetLevelSetParas(){return NULL;};
    virtual void SetThresholdValue(double thresholdValue){return;}
    virtual double GetThresholdValue(){return 0.;}

  protected:
      vtkPlane * m_vtkPlaneGeometry;
      std::array<double,3> m_CenterPoint;
      std::array<double,3> m_ScalingPoint;
      int m_ControlPointSelectedIndex;
      int m_MinControlPointNumber;
      int m_MaxControlPointNumber;
      std::vector<std::array<double,3> > m_ControlPoints;
      std::vector<std::array<double,3> > m_ContourPoints;
}
```

**circleContour**
```
class SV_EXPORT_SEGMENTATION circleContour : public Contour
{
  public:
    virtual circleContour* Clone() override;
    virtual std::string GetClassName() override;
    virtual void SetControlPoint(int index, std::array<double,3> point) override;

  protected:
    no members
}
```

**levelSetContour**
```
class SV_EXPORT_SEGMENTATION levelSetContour : public Contour
{
  public:

  protected:
    svLSParam* m_paras;
    bool m_forceClosed;
}
```

**ContourPolygon**
```
class SV_EXPORT_SEGMENTATION ContourPolygon : public Contour
{
  public:
  protected:
    no members
}
```

**thresholdContour**
```
class SV_EXPORT_SEGMENTATION thresholdContour : public Contour
{
  public:

  protected:
    double m_thresholdValue;
    bool m_forceClosed;
}
```



# Current Design

The API refences object via string names and a Tcl repository.

API types are defined for:
* Contour - sv3::Contour* geom
* Geometry - cvPolyData only through repository
* Mesh - cvMeshObject* geom
* Path - sv3::PathElement* geom
* SolidModel - cvSolidModel* geom

These types just store a reference to an SV object (all called geom!). 
