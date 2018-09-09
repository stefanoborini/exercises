sum = 0
for i in xrange(1,1000):
    if (not (i%3 and i%5)):
        print i
        sum+=i
print sum
