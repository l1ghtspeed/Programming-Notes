import copy

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i in range(len(nums)):
            num = nums[i]
            temp = copy.deepcopy(ans)
            for arr in temp:
                arr = list(arr)
                if num >= arr[-1]:
                    arr.append(num)
                    ans.add(tuple(arr))
            for j in range(i):
                if num >= nums[j]:
                    ans.add((nums[j], num))

        return ans
