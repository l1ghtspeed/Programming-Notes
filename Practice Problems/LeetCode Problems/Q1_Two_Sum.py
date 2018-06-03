# The solutions below are for Question 1 of LeetCode - Two Sum:
#
# Problem Description:
# Given an array of integers, return the indices of the two array elements that add to a target.
# 
# Difficulty: Easy


# Naive solution - double for loop:
# Time complexity: O(n^2)
# Space complexity: O(n)

def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] + arr[j] == target):
                return [i, j]


# Faster Solution - Single Run Hashmap:
# Time complexity: O(n)
# Space complexity: O(n)

