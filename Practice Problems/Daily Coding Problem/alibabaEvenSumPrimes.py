'''
This problem was asked by Alibaba.

Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:

Input: 4
Output: 2 + 2 = 4
If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

[a, b] < [c, d]
If a < c OR a==c AND b < d.
'''

def primesum(n):
    for i in xrange(2, n):
        if isPrime(i) and isPrime(n - i):
            return i, n - i

def isPrime(n):
    if n < 2:
        return False
    for i in xrange(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True
