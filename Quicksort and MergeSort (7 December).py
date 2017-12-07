import matplotlib.pyplot as plt
import math
import os
from random import randint
from timeit import Timer
import timeit

def genrandomnumbers(length): # GENERATE length RANDOM NUMBERS  IN RANGE 1-maxval
    maxval = 10000000
    string = ""
    for n in range(length):
        string += str(randint(1,maxval))+" "
    L=list(map(int,string.split()))
    return L
    
def qsort(L):
    if len(L) <= 1:
        return(L)
    else:
        pivot=L[0]
        L1 = [x for x in L[1:] if x <= pivot]
        L2 = [x for x in L[1:] if x > pivot]
        L1 = qsort(L1)
        L2 = qsort(L2)
        return L1+[pivot]+L2

def mergesort(L):
    if len(L)<=1:
        return(L)
    else:
        center=len(L)//2
        L1 = L[:center]
        L2=L[center:]
        L1=mergesort(L1)
        L2=mergesort(L2)
    return mergeleftright(L1,L2)

def mergeleftright(L1,L2):
    i=0
    j=0
    n=len(L1)
    m=len(L2)
    o=[]
    while i<n and j<m:
        if L1[i]<=L2[j]:
            o.append(L1[i])
            i=i+1
        else:
            o.append(L2[j])
            j=j+1
    if i==n:
        o+=L2[j:]
    else:
        o+=L1[i:]
    return o        

def writef(filename,myres):
    with open(filename,"a") as f:
        text=myres
        f.write('{}'.format(text))
    return

if __name__=='__main__':
    os.chdir("C:/Users/rober/Desktop/Data")
    maxpoweroften=5
    numberoftests=5
    qsort_times=""
    mergesort_times=""

    for nrtest in range(numberoftests):
        for dim in [10**p for p in range(1,maxpoweroften+1)]:
            L=genrandomnumbers(dim)
#                    TIMES FOR QUICKSORT IN A STRING
            funcname="qsort("+str(L)+")"
            t1=Timer(funcname,"from __main__ import qsort")
            qsort_times+=str(timeit.timeit(funcname,setup="from __main__ import qsort",number=1))+" "

#                    TIMES FOR MERGESORT IN A STRING
            funcname="mergesort("+str(L)+")"
            t1=Timer(funcname,"from __main__ import mergesort")
            mergesort_times+=str(t1.timeit(3))+" "
        qsort_times+="\n"
        mergesort_times+="\n"
        
#                    WRITE STRINGS ON FILES                    
    writef("quicksort.txt",qsort_times)
    writef("mergesort.txt",mergesort_times)

filenames = ["quicksort", "mergesort"]

def readf(filename):
    with open(filename, "r") as f:
        r_n = f.readline()
    return r_n


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

    N = [10 ** p for p in range(1, maxpoweroften + 1)]

    fig = plt.figure()
    # myplot = plt.plot(N, mintimes, 'vg--', N, meantimes, "vb--", N, maxtimes, "vr--")
    myplot = plt.plot(N, meantimes, "vb--")
    plt.xscale('log', basex=10)
    # plt.yscale('log',basey=10)
    # plt.ylim(10**-6,1)
    # plt.show()
    fig.savefig(filein + ".png")



    
