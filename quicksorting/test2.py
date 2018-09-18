
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

    leftview=view(a,4)
    rightview=view(a,4)
    v = rightview[r]
    while 1:
        i=i+1
        while leftview[i] < v:
            i=i+1
      
        j=j-1
        while v < rightview[j]:
            j=j-1
            if j == l:
                break
        if (i >= j ):
            break
        t = leftview[i]
        leftview[i] = rightview[j]
        rightview[j] = t 
    t = leftview[i]
    leftview[i] = rightview[r]
    rightview[r] = t
    return i

class view(object):
    def __init__(self, a, viewsize):
        self.viewsize=viewsize
        self.viewarray=[]
        self.array=a
        self.viewpos=-1
        self.dirty=False
    def __getitem__(self,item):
        viewpos, offset = self.abs2Rel(item)
        if viewpos != self.viewpos:
            self.pageout()
            self.pagein(viewpos)
        return self.viewarray[offset]
    def __setitem__(self, item, value):
        viewpos, offset = self.abs2Rel(item)
        if viewpos != self.viewpos:
            self.pageout()
            self.pagein(viewpos)
        self.viewarray[offset]=value
        self.dirty=True

    def abs2Rel(self, absaddr):
        viewpos = absaddr / self.viewsize
        offset = absaddr % self.viewsize
        return (viewpos, offset)

    def rel2Abs(self, viewpos, offset):
        return viewpos*self.viewsize+offset

    def overlap(self, v):
        if self.viewsize == v.viewsize: return self.viewpos == v.viewpos
        return ( self.startpos <= v.startpos <= self.stoppos or \
             self.startpos <= v.stoppos <= self.stoppos)
    def pagein(self,viewpos):
        self.viewpos=viewpos
        print "pagein chunk ",viewpos
        self.startpos = self.viewpos*self.viewsize
        if self.startpos + self.viewsize >= len(self.array):
            self.viewrealsize = len(self.array) - self.startpos
        else:
            self.viewrealsize = self.viewsize 
        self.stoppos=self.startpos+self.viewrealsize
        self.viewarray=self.array[self.startpos:self.stoppos]        
        self.dirty=False
    def pageout(self):
        if not self.dirty: return
        print "pageout dirty chunk ",self.viewpos
        self.array[self.startpos:self.stoppos]=self.viewarray
        self.dirty=False
    def dispose(self):
        self.pageout()
#chunksize=7
#leftview=[]
#arraysize=15
#array=range(0,arraysize)
#
#largepos=13
#(leftview,viewpos,len,chunkpos)=chunk(array,largepos,chunksize,arraysize)
#
#print leftview, viewpos, len, chunkpos
#print "searched = ", leftview[chunkpos]


import random
a=[]
for i in xrange(1,15):
    a.append(random.randrange(100))

print "begin sorting"
#a=[24, 108, 122, 185, 207, 234, 300, 408, 512, 523, 562, 582, 649, 703, 720, 777, 866, 894, 967]
qsort(a,0,len(a)-1)
print a
