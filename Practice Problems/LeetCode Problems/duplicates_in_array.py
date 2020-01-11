class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            n = nums[i]
            if n != i+1 and nums[n-1] != n:
                nums[i] , nums[n-1] = nums[n-1], n
            else:
                i+=1
        return [num for i, num in enumerate(nums) if num != i+1]
