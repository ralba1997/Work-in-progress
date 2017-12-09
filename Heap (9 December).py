# -*- coding: utf-8 -*-
class BinHeap:
    def __init__(self):
        self.name = None
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self,i):
        while i // 2 > 0:
             if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
             i = i // 2
          
    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1
              
    def maxChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] > self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval
      
    def findMax(self):    
      n=self.currentSize
      retval=self.maxChild(n//4+1)
      for i in range((n//4+2),n//2+1):
          if self.heapList[self.maxChild(i)]>self.heapList[retval]:
              retval=self.maxChild(i)
      return retval
    
    def delMax(self):
      retval = self.findMax()
      self.heapList.pop(retval)       
      self.currentSize = self.currentSize - 1
      return retval

    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1

def genrandomnumbers(length): # GENERATE length RANDOM NUMBERS  IN RANGE 1-maxval
    maxval=10000000
    string=""
    for n in range(length):
        string+=str(randint(1,maxval))+" "
    L=list(map(int,string.split()))
    return L

def insertnumbersinheap(aheap, alist):
    aheap.buildHeap(alist)
    return aheap
    
def heapfindmax(aheap):
    return aheap.findMax()

def heapdelmax(aheap):
    return aheap.delMax()

def gettime(funcname, param, param2):
    if param2 == "":
        fn = funcname.__name__ + "(" + param.name + ")"
    else:
        fn = funcname.__name__ + "(" + param.name + "," + str(param2) + ")"
    setpar = "from __main__ import " + funcname.__name__ + "," + param.name
    t1 = Timer(fn, setpar)
    time = str(t1.timeit(1)) + " "
    return time
    
def writef(filename,myres):
    with open(filename,"w") as f:
        text=myres
        f.write('{}'.format(text))
    return

def readf(filename):
    with open(filename,"r") as f:
        r_n=f.readline()
    return r_n    

from timeit import Timer
import timeit
from random import randint  
import matplotlib.pyplot as plt
import math
import os

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)
if not os.path.exists("Data"):
    os.makedirs("Data")
os.chdir(path + "\Data")

maxpoweroften=6
numberoftests=5

filenames=["heapinsertion","heapfindmax","heapdelmax"]
heapinsertion_times=""
heapfindmax_times=""
heapdelmax_times=""
for nrtest in range(numberoftests):
    for dim in [10**p for p in range(1,maxpoweroften+1)]:
        L=genrandomnumbers(dim)
        myheap = BinHeap()
        myheap.name = "myheap"
        time=gettime(insertnumbersinheap, myheap, L)
        heapinsertion_times+=time
        time=gettime(heapfindmax, myheap, "")
        heapfindmax_times+=time
        time=gettime(heapdelmax, myheap, "")
        heapdelmax_times+=time
    heapinsertion_times+="\n"
    heapfindmax_times+="\n"
    heapdelmax_times+="\n"
writef("heapinsertion.txt",heapinsertion_times)
writef("heapfindmax.txt",heapfindmax_times)
writef("heapdelmax.txt",heapdelmax_times)

for filein in filenames:

    filename = filein + ".txt"
    t = []
    with open(filename, "r") as f:
        for i in range(numberoftests):
            t.append(list(map(float, f.readline().split())))

    # maxtimes = []
    # mintimes = []
    meantimes = []
    for j in range(maxpoweroften):
        # mintimes.append(min(t[i][j] for i in range(numberoftests)))
        # maxtimes.append(max(t[i][j] for i in range(numberoftests)))
        sumt = sum(t[i][j] for i in range(numberoftests))
        meantimes.append(sumt / numberoftests)

    if filein == "heapinsertion":
        heapinsertiontimes = meantimes
    elif filein == "heapfindmax":
        heapfindmaxtimes = meantimes
    elif filein == "heapdelmax":
        heapdelmaxtimes = meantimes

    N = [10 ** p for p in range(1, maxpoweroften + 1)]

fig = plt.figure()
plt.plot(N, heapinsertiontimes, "vb--")
plt.plot(N, heapfindmaxtimes, "vr--")
plt.plot(N, heapdelmaxtimes, "vg--")
plt.xscale('log', basex=10)
plt.yscale('log', basey=10)
plt.title("Heap")
plt.xlabel("Length of list of random numbers")
plt.ylabel("Times")
axes = plt.gca()
axes.set_ylim([10**(-6), 10**2])
# plt.ylim(10**-6,1)
# plt.show()
fig.savefig("Heap.png")



