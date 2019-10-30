
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

The **static cvFactoryRegistrar gRegistrar** class data is used to 



**Contour**
```
class SV_EXPORT_SEGMENTATION Contour : public cvRepositoryData
{
  public:
    struct svLSParam { double ctrx; double ctry; double ctrz; ... }
    
    static cvFactoryRegistrar gRegistrar;
      
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

## cvFactoryRegistrar

This is used in
```
sv/Mesh/AdaptObject/sv_AdaptObject.h:    static cvFactoryRegistrar gRegistrar;
sv/Mesh/AdaptObject/sv_adapt_init_py.h:  cvFactoryRegistrar* registrar;
sv/Model/SolidModel/sv_SolidModel.h:     static cvFactoryRegistrar gRegistrar;
sv/Model/SolidModel/sv_solid_init_py.h:  cvFactoryRegistrar* registrar;
sv3/Segmentation/sv3_Contour_init_py.h:  cvFactoryRegistrar* registrar;
sv3/Segmentation/sv3_Contour.h:          static cvFactoryRegistrar gRegistrar;
```




```
class SV_EXPORT_UTILS cvFactoryRegistrar {
  public:
    cvFactoryRegistrar();

    FactoryMethodPtr GetFactoryMethodPtr( int factory_type );
    void SetFactoryMethodPtr( int factory_type, FactoryMethodPtr factory_ptr );

    // Returns a pointer to whatever you've created with a factory
    void* UseFactoryMethod( int factory_type );

  protected:
    FactoryMethodPtr factoryMethodPtrs[CV_MAX_FACTORY_METHOD_PTRS];

};
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

## Contour Base and Derived Classes

Drived classes constructors are set and accessed from the **ContourObjectRegistrar** PyObject using
```
 PyObject* pyGlobal = PySys_GetObject("ContourObjectRegistrar");
```

Each derived class module sets it constuctor in its **PyMODINIT_FUNC** function
```
contourObjectRegistrar->SetFactoryMethodPtr( cKERNEL_CIRCLE, (FactoryMethodPtr) &CreateCircleContour );
contourObjectRegistrar->SetFactoryMethodPtr( cKERNEL_LEVELSET, (FactoryMethodPtr) &CreatelevelSetContour );
contourObjectRegistrar->SetFactoryMethodPtr( cKERNEL_SPLINEPOLYGON, (FactoryMethodPtr)&CreateSplinePolygonContour);
```

A Contour object is created using the following steps
```
sv.contour.set_contour_kernel('Circle')
cont = sv.contour.Contour()
cont.new_object(name, path_name, index)
```

The **Contour.new_object()** method calls **sv3::Contour::DefaultInstantiateContourObject()** to create a new Contour derived objecy using
```
PyObject* pyGlobal = PySys_GetObject("ContourObjectRegistrar");
contour = (Contour*)gRegistrar.UseFactoryMethod(t);
```



