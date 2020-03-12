from collections import deque
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        q, d, ans = deque([(headID, 0)]), {}, 0
        for i, man in enumerate(manager):
            if man not in d:
                d[man] = []
            d[man].append(i)
        while q:
            man, time = q.popleft()
            if man not in d:
                ans = max(ans, time)
                break
            for emp in d[man]:
                q.append((emp, time+informTime[man]))
        return ans
                
