all: main module1 module2

main: main.cpp Base.cpp
	g++ -I. main.cpp Base.cpp -o main -ldl
	
module1:
	g++ -I. -shared -rdynamic -fPIC Base.cpp Module1.cpp -o Module1.so
module2:
	g++ -I. -shared -rdynamic -fPIC Base.cpp Module2.cpp -o Module2.so


clean:
	rm *.o *.so main
