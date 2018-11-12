'''
Largest Prime Factor

Problem Description:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

import math

n = 600851475143

while n%2 == 0:
    n = n/2

for i in range(3, int(math.sqrt(n))+2, 2):
    while n%i == 0:
        if n/i == 1:
            print(n)
        else:
            n = n/i
    
