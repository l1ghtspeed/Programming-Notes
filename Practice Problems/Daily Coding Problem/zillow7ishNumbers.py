'''

Problem Description:

This problem was asked by Zillow.

Let's define a "sevenish" number to be one which is either a power of 7, or the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, and so on. Create an algorithm to find the nth sevenish number.

'''

def solve(n):

    ret = 0
    bit_place = 0

    while n:
        if (n & 1):
            ret += 7 ** bit_place

        n >>= 1
        bit_place += 1

    return ret