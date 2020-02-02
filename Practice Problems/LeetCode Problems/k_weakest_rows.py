import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        q = []
        for i in range(len(mat)):
            count = 0
            for num in mat[i]:
                if num == 1:
                    count += 1
                else:
                    break
            
            heapq.heappush(q, (count, i))
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(q)[1])
        return ans
