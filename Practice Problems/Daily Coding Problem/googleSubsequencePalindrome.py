'''
Problem Description:

This problem was asked by Google.

Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.

'''


def longest_palindromic_subsequence(s):
    if s == s[::-1]:
        return len(s)

    n = len(s)
    A = [[0 for j in range(n)] for i in range(n)]

    for i in range(n - 1, -1, -1):
        A[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                A[i][j] = 2 + A[i + 1][j - 1]
            else:
                A[i][j] = max(A[i + 1][j], A[i][j - 1])

    return A[0][n - 1]
