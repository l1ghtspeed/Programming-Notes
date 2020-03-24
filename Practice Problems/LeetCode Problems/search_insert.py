class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        l, r = 0, len(nums)-1
        while l < r - 1:
            c = (l + r) // 2
            if nums[c] == target:
                return c
            elif nums[c] < target:
                l = c
            else:
                r = c
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        if nums[l] > target:
            if l == 0:
                return 0
            return l - 1
        if nums[r] < target:
            return r + 1
        return l + 1
