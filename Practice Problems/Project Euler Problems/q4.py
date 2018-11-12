# coding=utf-8

'''
Largest Palindrome Product

Problem Description:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindromic(n):
    n = str(n)
    for i in range(len(n)//2):
        if n[i] != n[len(n)-i-1]:
            return False
    return True

largest = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        if isPalindromic(i*j):
            if i*j > largest:
                largest = i*j
            
print(largest)



    
    

