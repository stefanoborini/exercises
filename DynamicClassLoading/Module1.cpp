#include <Module1.h>
#include <iostream>

Module1::Module1() {
	std::cout << "Module1 constructor" << std::endl;
}
Module1::~Module1() {
	std::cout << "Module1 destructor" << std::endl;
}
void Module1::method() {
	std::cout << "Module1 method" << std::endl;
}

Base * Module1_create() {
	return new Module1();
}

