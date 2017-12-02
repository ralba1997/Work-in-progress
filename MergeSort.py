L = list(map(int, input().split()))
print(L)


def mergesort(L):
    if len(L) <= 1:
        return L
    else:
        center = len(L) // 2
        L1 = L[:center]
        L2 = L[center:]
        L1 = mergesort(L1)
        L2 = mergesort(L2)
    return mergeleftright(L1, L2)


def mergeleftright(L1, L2):
    i = 0
    j = 0
    n = len(L1)
    m = len(L2)
    o = []

    while i < n and j < m:
        if L1[i] <= L2[j]:
            o.append(L1[i])
            i = i + 1
        else:
            o.append(L2[j])
            j = j + 1
    if i == n:
        o += L2[j:]
    else:
        o += L1[i:]

    return o


print(mergesort(L))
