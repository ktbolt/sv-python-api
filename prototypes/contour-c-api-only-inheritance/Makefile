
src = Contour.cpp CircleContour.cpp contour_module.cpp
obj = $(src:.cpp=.o) 

# Shared library name must match the module name.
lib = lcontour.dylib
lib = contour.so

pdir= /usr/local/Cellar/python/3.6.5_1/Frameworks/Python.framework/Versions/3.6
inc=-I$(pdir)/Headers

flags=-std=c++11 
flags=-std=c++11 -fPIC $(inc)

libs=-L$(pdir)/lib -lpython3.6

$(lib): $(obj)
	g++ -shared -o $(lib) $(obj) $(libs) $(link_flags)

Contour.cpp.o: Contour.h
	g++ $(flags) -c $<

CircleContour.cpp.o: CircleContour.h
	g++ $(flags) -c $<

.cpp.o: 
	g++ $(flags) -c $<

clean:
	rm -f *.o *.so *.dylib;


