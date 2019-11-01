
src = p.cpp Contour.cpp CircleContour.cpp 
obj = $(src:.cpp=.o) 

flags=-std=c++11 
flags=-std=c++11 -fPIC $(inc)

p: $(obj)
	g++ -o p $(obj) 

Contour.cpp.o: Contour.h
	g++ $(flags) -c $<

CircleContour.cpp.o: CircleContour.h
	g++ $(flags) -c $<

.cpp.o: 
	g++ $(flags) -c $<

clean:
	rm -f *.o *.so *.dylib;


