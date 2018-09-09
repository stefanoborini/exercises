#include <Base.h>

class Module1 : public Base {
public:
	Module1();
	virtual ~Module1();
	virtual void method();
};

extern "C" {
	Base * Module1_create();
}
