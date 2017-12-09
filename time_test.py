import quicksort as qs
import mergesort as ms
import binary_tree as bt
import heap as heap
import random
import timeit

import matplotlib.pyplot as plt
import numpy as np


for i in range(1,5):
    for i in ms.lll:
        time_ms=timeit.timeit("ms.mergesort(ms.lll)", number=5, globals=globals())
    for i in qs.lll:
        time_qs=timeit.timeit("qs.quick_sort(qs.lll)", number=5, globals=globals())
    for i in bt.lll:
        time_tree_insert = timeit.timeit('bt.h.insert(bt.e)', number=5, globals=globals())
        time_tree_getrandom = timeit.timeit('bt.h.insert(bt.e)', number=5, globals=globals())
        time_tree_delrandom = timeit.timeit('bt.h.insert(bt.e)', number=5, globals=globals())
        time_tree_Max = timeit.timeit('bt.h.insert(bt.e)', number=5, globals=globals())
    for i in heap.lll:
        time_heap_insertion = timeit.timeit('heap.h.insert(heap.lll)', number=5, globals=globals())
        time_heap_getMax = timeit.timeit("heap.mergesort(heap.lll)", number=5, globals=globals())
time_heap_delMax = timeit.timeit("heap.mergesort(heap.lll)", number=5, globals=globals())
