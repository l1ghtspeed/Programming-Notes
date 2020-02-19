class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        l1, l2 = len(nums1), len(nums2)
        memo = [[[-1 for _ in range(l1+1)] for _ in range(l2+1)] for _ in range(k+1)]
        def recurse(i, j, k):
            ans = []
            if memo[k][j][i] != -1:
                return memo[k][j][i]
            if k == 1:
                if nums1[i:] or nums2[j:]:
                    ans = [max(nums1[i:] + nums2[j:])]
            elif k > 1:
                paths = []
                if i < l1:
                    paths.append([nums1[i]] + recurse(i+1, j, k-1))
                    paths.append(recurse(i+1, j, k))
                if j < l2:
                    paths.append([nums2[j]] + recurse(i, j+1, k-1))
                    paths.append(recurse(i, j+1, k))
                if paths:
                    ans = paths[self.max_path(paths)]
            memo[k][j][i] = ans
            return ans
        return recurse(0, 0, k)
    
    def max_path(self, paths):
        p = []
        for path in paths:
            s = 0
            for i, num in enumerate(path):
                s += num * 10 ** (len(path) - i)
            p.append(s)
        return p.index(max(p))
        
