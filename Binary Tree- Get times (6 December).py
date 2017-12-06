def genrandomnumbers(length):  # GENERATE length RANDOM NUMBERS  IN RANGE 1-maxval
    maxval = 1000000
    string = ""
    for n in range(length):
        string += str(randint(1, maxval)) + " "
    L = list(map(int, string.split()))
    return L


def insertnumbersintree():
    for i in range(len(L)):
        mytree.put(L[i], L[i])
        # insertnumber(L[i])
    return mytree


def gettime(funcname, param):
    fn = funcname.__name__ + "(" + str(param) + ")"
    setpar = "from __main__ import " + funcname.__name__
    t1 = Timer(fn, setpar)
    time = str(t1.timeit(1)) + " "
    return time


def getrelement(element):
    relemvalue = mytree.get(element)
    return relemvalue


def maxelement():
    # maxnodevalue=mytree.root.findMax()
    maxnodevalue = mytree.root.findMax().val
    return maxnodevalue


def delrelement(element):
    # ver_relement(element,mytree)
    mytree.delete(element)
    # ver_relement(element,mytree)


def ver_relement(element, atree):
    # print "index=", r
    # elem = L[r]
    print("elem=", element)
    print("list element " + str(r) + " =" + str(elem) + "in tree?", elem in atree, " ===>", atree.get(elem))


def ver_randomnumbers(length, S):
    print("   dim=", length, "    L=", S)


def ver_tree(atree, alist):
    print()
    print("Show tree")
    print("Size=", atree.size, "     Root=", atree.root.key)
    for i in range(len(alist)):
        l = alist[i]
        print("list element " + str(i) + " =" + str(l) + " in mytree?", l in atree, " ===>", atree.get(l))


def ver_maxelement(atree, alist, maxnodevalue):
    maxlist = max(alist)
    print("maxlist=", maxlist)
    print("maxnodevalue=", maxnodevalue)


def writef(filename, myres):
    with open(filename, "w") as f:
        text = myres
        f.write('{}'.format(text))
    return


from timeit import Timer
import timeit
from random import randint
import os

gettimes = True
os.chdir("C:/Users/rober/Desktop/Data")
maxpoweroften = 5
numberoftests = 3

if gettimes:
    insertion_times = ""
    getrandomelement_times = ""
    findmax_times = ""
    delrandomelement_times = ""
    for nrtest in range(numberoftests):
        for dim in [10 ** p for p in range(1, maxpoweroften + 1)]:
            print("nrtest=", nrtest, "dim=", dim)
            L = genrandomnumbers(dim)
            mytree = BinarySearchTree()
            time = gettime(insertnumbersintree, "")
            insertion_times += time
            r = randint(0, len(L) - 1)
            elem = L[r]
            time = gettime(getrelement, elem)
            getrandomelement_times += time
            time = gettime(maxelement, "")
            findmax_times += time
            r = randint(0, len(L) - 1)
            elem = L[r]
            time = gettime(delrelement, elem)
            delrandomelement_times += time
        insertion_times += "\n"
        getrandomelement_times += "\n"
        findmax_times += "\n"
        delrandomelement_times += "\n"
        # print "insertion times=          ",insertion_times
    # print "get randomelement times=  ",getrandomelement_times
    # print "findmax times=            ",findmax_times
    # print "del randomelement times=  ",delrandomelement_times
    writef("insertion.txt", insertion_times)
    writef("getrandomelement.txt", getrandomelement_times)
    writef("maxtree.txt", findmax_times)
    writef("delrandomelement.txt", delrandomelement_times)
else:
    for dim in (10, 100):
        L = genrandomnumbers(dim)
        ver_randomnumbers(dim, L)
        mytree = BinarySearchTree()
        mytree = insertnumbersintree()
        ver_tree(mytree, L)
        r = randint(0, len(L) - 1)
        elem = L[r]
        print("random element in list=", elem)
        relement = getrelement(elem)
        print("random element in tree=", relement)
        maxintree = maxelement()
        print("max element in tree=", maxintree)
        ver_maxelement(mytree, L, maxintree)
        r = randint(0, len(L) - 1)
        elem = L[r]
        print("random element in list=", elem)
        delrelement(elem)
        ver_tree(mytree, L)
