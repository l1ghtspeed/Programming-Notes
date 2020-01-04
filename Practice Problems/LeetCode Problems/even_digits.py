class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            stringified = str(num)
            count += 1 - len(stringified) % 2
        return count
