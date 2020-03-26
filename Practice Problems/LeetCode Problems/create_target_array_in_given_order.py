class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            pos = index[i]
            if pos == len(ans):
                ans.append(nums[i])
            else:
                ans = ans[:pos] + [nums[i]] + ans[pos:]
        return ans
