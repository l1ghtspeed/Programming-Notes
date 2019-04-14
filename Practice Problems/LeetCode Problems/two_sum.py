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
def twoSum(self, nums: List[int], target: int) -> List[int]:
    d = {}
    for i in range(len(nums)):
        if nums[i] in d:
            return [d[nums[i]], i]
        else:
            d[target-nums[i]] = i



def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        substring = ''
        if strs:
            for i in range(len(strs[0])):
                for j in strs:
                    if i >= len(j):
                        return substring
                    elif strs[0][i] != j[i]:
                        return substring
                substring += strs[0][i]
        return substring


def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        solutions = []
        
        d = {}
        for i in strs:
            if (i in d):
                d[i] = d[i] + 1
            else:
                d[i] = 1
        
        for key in d:
            tempSol = []
            tempSol.append(key)
            for key2 in d:
                if (key2 != key) and self.isAnagram(key, key2):
                    tempSol.append(key2)
                    del d[key2]
            solutions.append(tempSol)
            del d[key]
        
        return solutions
    
    def isAnagram(self, s1, s2):
        s_1 = [0]*26
        s_2 = [0]*26
        
        for i in range(len(s1)):
            pos = ord(s1[i])-ord('a')
            s_1[pos] = s_1[pos] + 1

        for i in range(len(s2)):
            pos = ord(s2[i])-ord('a')
            print(pos)
            print(s_2)
            s_2[pos] = s_2[pos] + 1

        for i in range(26):
            if s_1[i] != s_2[i]:
                return False

        return True
