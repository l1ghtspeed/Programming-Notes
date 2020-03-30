class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.helper(nums, target, True)
        if l == len(nums) or nums[l] != target:
            return [-1, -1]
        return [l, self.helper(nums, target, False) - 1]
        
    def helper(self, nums, target, f):
        l, r = 0, len(nums)
        while l < r:
            c = (l + r) // 2
            if nums[c] > target or (f and nums[c] == target): r = c
            else: l = c + 1
        return l
