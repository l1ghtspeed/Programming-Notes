class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or k == 0:
            return
        
        start, count = 0, 0
        while count < len(nums):
            ind, temp = start, nums[start]
            while True:
                ind = (ind+k)%len(nums)
                new_temp = nums[ind]
                nums[ind] = temp
                temp = new_temp
                count += 1
                if ind == start or count == len(nums):
                    break
            start += 1
            
