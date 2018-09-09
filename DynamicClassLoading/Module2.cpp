#include <Module2.h>
#include <iostream>

Module2::Module2() {
	std::cout << "Module2 constructor" << std::endl;
}
Module2::~Module2() {
	std::cout << "Module2 destructor" << std::endl;
}
void Module2::method() {
	std::cout << "Module2 method" << std::endl;
}

Base * Module2_create() {
	return new Module2();
}

