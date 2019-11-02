
src=Contour.cpp CircleContour.cpp contour_module.cpp
obj=$(src:.cpp=.o) 
headers=contour_module.h circle_contour_module.h contour_module_kernel.h 

# Shared library name must match the module name.
lib = contour.dylib
lib = contour.so

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

$(lib): $(obj) 
	g++ -shared -o $(lib) $(obj) $(libs) $(link_flags)

Contour.o: Contour.cpp Contour.h
	g++ $(flags) -c $<

contour_module.o: contour_module.cpp $(headers)
	g++ $(flags) -c $<

CircleContour.o: CircleContour.cpp CircleContour.h
	g++ $(flags) -c $<

.cpp.o: 
	g++ $(flags) -c $<

clean:
	rm -f *.o *.so *.dylib;


