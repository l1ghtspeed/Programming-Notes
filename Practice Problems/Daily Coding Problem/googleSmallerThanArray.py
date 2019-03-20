'''

Problem Description:

This problem was asked by Google.

Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1

'''

# naive solution with n^2 runtime
def naive_solution(a):
    newA = []
    for i in range(len(a)):
        count = 0
        for j in range(i):
            if (a[j] < a[i]):
                count += 1
        newA.append(count)
    return newA

# efficient solution with nlogn runtime (uses a sorted list) and n space
import bisect

def efficient_solution(a):
    result = []
    s = []
    for num in reversed(lst):
        i = bisect.bisect_left(s, num)
        result.append(i)
        bisect.insort(s, num)
    return list(reversed(result))