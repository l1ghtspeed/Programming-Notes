from math import log
from random import sample

def find_median(array, precision):
    m = precision * int(log(len(array), 2))

    subset = sample(array, m)
    subset.sort()

    return subset[m // 2]
