#include <iostream>
#include <Base.h>
#include <stdio.h>

#include <dlfcn.h>

int main() {
	std::string name;
	std::cin >> name;

	std::string soname = "./"+ name + ".so";
	std::string symname = name + "_create";

	const char *cstring = soname.c_str();
	void *handle = dlopen(cstring, RTLD_NOW);
	cstring = symname.c_str();
	void *symbol = dlsym(handle, cstring);
	Base *entity = ((Base * (*)())symbol)();

	entity->method();

	delete entity;
}
