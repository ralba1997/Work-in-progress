class TreeNode:
    def __init__(self, key, val, count, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.count = count
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild
        
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self       

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent 

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def replaceNodeData(self, key, value, count, lc, rc):
        self.key = key
        self.val = value
        self.count = count
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                    self.rightChild.parent = self.parent

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
                yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

    def findMin(self):
        current = self             
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def findMax(self):
        current = self                   
        while current.hasRightChild():
            current = current.rightChild
        return current


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val, count):
        if self.root:
            self._put(key, val, count, self.root)
        else:
            self.root = TreeNode(key, val, count)
        self.size = self.size + count
        
    def _put(self, key, val, count, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, count, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, count, parent=currentNode)
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(key, val, count, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, count, parent=currentNode)
        else:
            currentNode.count += count
            
    def __setitem__(self, k, v, c):
        self.put(k, v, c)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.val
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)
    
    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False
            
    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size-nodeToRemove.count
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)
    
    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():  # interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.val = succ.val
        else:  # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.val,
                                                currentNode.leftChild.count,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.val,
                                                currentNode.rightChild.count,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)


#                    GENERATE dim RANDOM NUMBERS  IN RANGE 1-maxval
from random import randint
string = ""
dim = 10
maxval = 10000
for k in range(dim):
        string += str(randint(1, maxval))+" "
L = list(map(int, string.split()))
print(L)
n = len(L)

#                     INSERT NUMBERS IN BINARY TREE
mytree = BinarySearchTree()
for i in range(n):
    mytree.put(i, L[i], 1)

#                     VERIFY INSERTION
print()
print("VERIFY INSERTION")
print("size=", mytree.size, "   root=", mytree.root.val)
for i in range(n):
    print(i, mytree.get(i))

#                      GET RANDOM ELEMENT       
print()
print("GET RANDOM ELEMENT")
r = randint(0, n-1)
print("random index=", r)
print("mytree.get(", r, ")=", mytree.get(r))

#                      GET MAX
print()
print("GET MAX")
print("findMax=", mytree.root.findMax().val)

#                      DELETE RANDOM ELEMENT 
print()
print("DELETE RANDOM ELEMENT")
r = randint(0, n-1)
print(r)
# print "value=",mytree.get(elem)
print("mytree.get(", r, ")=", mytree.get(r))
mytree.delete(r)

#                      VERIFY DELETION
print()
print("VERIFY DELETION")
print("size=", mytree.size, "   root=", mytree.root.val)
for i in range(n):
    print(i, mytree.get(i))

