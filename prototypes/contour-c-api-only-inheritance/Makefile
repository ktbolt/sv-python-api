
## Contour sources.
#
cont_src=Contour.cpp CircleContour.cpp PolygonContour.cpp contour_module.cpp
cont_obj=$(cont_src:.cpp=.o) 
cont_headers=contour_module.h circle_contour_module.h contour_module_kernel.h polygon_contour_module.h
# Shared library name must match the module name.
cont_lib = contour.dylib
cont_lib = contour.so

## Path sources.
#
path_src=Path.cpp path_module.cpp
path_obj=$(path_src:.cpp=.o) 
path_headers=path_module.h 
# Shared library name must match the module name.
path_lib = path.dylib
path_lib = path.so

OS := $(shell uname)

## MacOS
#
ifeq ($(OS),Darwin)
  pdir= /usr/local/Cellar/python/3.6.5_1/Frameworks/Python.framework/Versions/3.6
  inc=-I$(pdir)/Headers
  libs=-L$(pdir)/lib -lpython3.6

## Ubuntu
else
  inc=-I/usr/include/python3.5
  libs=-L/usr/lib/python3.5/config-3.5m-x86_64-linux-gnu -lpython3.5
endif

flags=-std=c++11 
flags=-std=c++11 -fPIC $(inc)

libs: $(path_lib) $(cont_lib) 

$(path_lib): $(path_obj) 
	g++ -shared -o $(path_lib) $(path_obj) $(libs) $(link_flags)

$(cont_lib): $(cont_obj) $(cont_headers)
	g++ -shared -o $(cont_lib) $(cont_obj) $(libs) ./path.so $(link_flags)

Contour.o: Contour.cpp Contour.h
	g++ $(flags) -c $<

contour_module.o: contour_module.cpp $(cont_headers)
	g++ $(flags) -c $<

CircleContour.o: CircleContour.cpp CircleContour.h
	g++ $(flags) -c $<

PolygonContour.o: PolygonContour.cpp PolygonContour.h
	g++ $(flags) -c $<


.cpp.o: 
	g++ $(flags) -c $<

clean:
	rm -f *.o *.so *.dylib;


