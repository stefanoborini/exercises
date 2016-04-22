import multipledispatch
import typecheck as tc

@multipledispatch.dispatch(int)
def foo(a):
    print("int ", a)


@multipledispatch.dispatch(str,int)
def foo(a, b):
    print("str int", a, b)


@tc.typecheck
def typechecking(foo: int) -> bool:
    print(foo)
    return True

foo(5)
foo("hello", 5)

print(typechecking(3))
