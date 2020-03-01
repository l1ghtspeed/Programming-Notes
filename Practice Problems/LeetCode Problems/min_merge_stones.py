# an interesting solution to something that doesn't work
import heapq
class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        ans, l, r, q = 0, 0, K-1, []
        while len(stones) >= K:
            curr = sum(stones[l:r+1])
            heapq.heappush(q, (curr, l, r+1))
            for i in range(len(stones)-K):
                r, l = r+1, l+1
                curr += stones[r] - stones[l-1]
                heapq.heappush(q, (curr, l, r+1))
            m = heapq.heappop(q)
            stones = stones[:m[1]] + [m[0]] + stones[m[2]:]
            ans, l, r, q = ans + m[0], 0, K-1, []
        if len(stones) == 1:
            return ans
        return -1    
