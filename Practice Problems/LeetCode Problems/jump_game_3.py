from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        seen = set()
        
        while q:
            num = q.popleft()
            
            if num not in seen and num >= 0 and num < len(arr):
                if arr[num] == 0:
                    return True
                q.append(num - arr[num])
                q.append(num + arr[num])
                seen.add(num)
        
        return False
            
