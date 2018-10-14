'''
Problem description

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.

'''

def solve(n):
    count = 0
    iterator = 1
    while count < n:
        iterator += 1
        if isPerfect(iterator):
            count += 1
    return iterator


def isPerfect(n):
    summ = 0
    while n > 10:
       summ += n % 10
       n = n // 10
    if summ == 10:
        return True
    return False