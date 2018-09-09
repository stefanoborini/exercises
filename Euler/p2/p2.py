def fib():
    a,b=1,2
    while True:
        yield a
        if a > 4000000:
            raise StopIteration
        a,b=b, a+b

sum=0
for n in (i for i in fib() if i % 2 == 0):
    sum+=n

print sum
