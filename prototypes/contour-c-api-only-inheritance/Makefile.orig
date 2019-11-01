
src = Contour.cpp
obj = $(src:.cpp=.o) 
lib = libcontour.so
inc=-I/usr/include/python3.5m

flags=-std=c++11 
flags=-std=c++11 -fPIC $(inc)

libs=-L/usr/lib/python3.5m -lpython3.5m

contour_module*.so: contour_module.cpp $(lib)
	python3 setup.py build_ext --inplace

$(lib): $(obj)
	g++ -shared -fPIC -o $(lib) $(obj) $(libs) $(link_flags)

.cpp.o: 
	g++ $(flags) -c $<

clean:
	rm -f *.o *.so;


