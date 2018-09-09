import itertools

def isPalindrome(x):
    digits=list(str(x))
    rev=list(reversed(digits))
    if digits == rev:
        return True

    return False

max = 0
for x,y in ( (a,b) for a in xrange(1000,100,-1) for b in xrange(1000,100,-1)):
    if isPalindrome(x*y) and x*y > max:
        max = x*y

print max
