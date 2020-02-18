class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, p1 = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if nums[p0] == 1:
                    nums[i] = nums[p1]
                    nums[p1] = 1  
                else:
                    nums[i] = nums[p0]
                nums[p0] = 0
                p0 += 1
                p1 += 1
            elif nums[i] == 1:
                temp = nums[p1]
                nums[p1] = nums[i]
                nums[i] = temp
                p1 += 1
