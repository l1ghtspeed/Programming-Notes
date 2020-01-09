# n^2 solution, currently TLE

from collections import deque

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        seen = set([0])
        q = deque([0])
        
        while q:
            elem = q.popleft()
            if elem == len(nums) - 1:
                return True
            for i in range(1, nums[elem]+1):
                pos_a, pos_b = i + elem, elem - i
                if pos_a < len(nums) and pos_a not in seen:
                    seen.add(pos_a)
                    q.append(pos_a)
                if pos_b >= 0 and pos_b not in seen:
                    seen.add(pos_b)
                    q.append(pos_b)
                
        return False

# n solution, uses dp, accepted

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        nums[-1] = 1
        for i in range(1, len(nums)):
            if nums[~i] >= nums[-i]:
                nums[~i] = 1
            else:
                nums[~i] = nums[-i] + 1
        
        return nums[0] == 1
