L = list(map(int, input().split()))
print(L)


def qsort(L):
    if len(L) <= 1:
        return L
    else:
        pivot = L[0]
        L1 = [x for x in L[1:] if x <= pivot]
        L2 = [x for x in L[1:] if x > pivot]
        L1 = qsort(L1)
        L2 = qsort(L2)
        return L1+[pivot]+L2


print(qsort(L))
