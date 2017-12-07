class BinHeap:
    def __init__(self):
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
      #print i,self.currentSize
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
      while i > 0:
          self.percDown(i)
          i = i - 1

bh = BinHeap()
# L=[9,5,6,2,3]
# L=[1000,70,20,100,4,90,95]
# L=[19,21,33,11,14,5,9,18,17,27,50]
L=[45,1745,73,64,27,36,74,6,2800,78,56,65,9999,57,21,34,9,10,100000,7,5,4,99,98,45,46,34]
print(L)
bh.buildHeap(L)
print(bh.heapList)
print("Max",bh.heapList[bh.findMax()])
print(bh.delMax())
print(bh.heapList)
#print(bh.delMin())
#print(bh.delMin())
#print(bh.delMin())
#print(bh.delMin())
