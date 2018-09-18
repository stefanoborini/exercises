
def qsort(a,l,r):
    stack=[]
    stack.append(l)
    stack.append(r)
    while len(stack) != 0:
        r=stack.pop()
        l=stack.pop()
        
        if r <= l:
            continue
        i = partition(a,l,r)
        if (i-l > r-i):
            stack.append(l)
            stack.append(i-1)
            stack.append(i+1)
            stack.append(r)
        else:
            stack.append(i+1)
            stack.append(r)
            stack.append(l)
            stack.append(i-1)
            

def partition(a,l,r):
    rightblock=[]
    leftblock=[]
    rightreallen=0
    leftreallen=0
    rightpos=r
    leftpos=l
     
    i = l-1
    j = r

    v = a[r]
    while 1:
        i=i+1
        while a[i] < v:
            i=i+1
      
        j=j-1
        while v < a[j]:
            j=j-1
            if j == l:
                break
        if (i >=j ):
            break
        t = a[i]
        a[i] = a[j]
        a[j] = t 
    t = a[i]
    a[i] = a[r]
    a[r] = t
    return i
    

import random
a=[]
for i in xrange(1,4000000):
    a.append(random.randrange(1000000))

print "begin sorting"
#a=[24, 108, 122, 185, 207, 234, 300, 408, 512, 523, 562, 582, 649, 703, 720, 777, 866, 894, 967]
qsort(a,0,len(a)-1)
print a
