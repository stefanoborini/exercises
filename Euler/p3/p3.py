import sys
import math

def isPrime(num):
    for i in xrange(int(math.sqrt(num)),2,-1):
        if num % i == 0:
            return False
    return True

num = 600851475143
for i in xrange(int(math.sqrt(num)),2,-1):
    if num % i == 0:
        if isPrime(i):
            print i
            sys.exit(0)
