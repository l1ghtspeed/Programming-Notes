class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans, N, P = [], [], []
        for num in A:
            if num < 0:
                N.append(num**2)
            elif num > 0:
                P.append(num**2)
            else:
                ans.append(num)
        p1, p2 = len(N)-1, 0
        while len(ans) < len(A):
            if p1 < 0:
                ans += P[p2:]
            elif p2 >= len(P):
                ans += N[:p1+1][::-1]
            elif N[p1] < P[p2]:
                ans.append(N[p1])
                p1 -=1
            else:
                ans.append(P[p2])
                p2 += 1
        return ans
