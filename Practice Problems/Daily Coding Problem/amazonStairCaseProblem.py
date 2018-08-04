''' 
Day 1

Problem: 

There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.

'''

def solveStaircase(n, x):
    arr = [0]*n
    for k in x:
        if (n - k >= 0):
            arr[n-k] = 1

    for i in range(n-1, -1, -1):
        for j in x:
            if (i - j >= 0):
                arr[i-j] += arr[i]
    return arr[0]

print(solveStaircase(4, [1, 2]))