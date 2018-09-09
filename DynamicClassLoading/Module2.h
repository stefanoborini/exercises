#include <Base.h>

class Module2 : public Base {
public:
	Module2();
	virtual ~Module2();
	virtual void method();
};

extern "C" {
	Base * Module2_create();
}
