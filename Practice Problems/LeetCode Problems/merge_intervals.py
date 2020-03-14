class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        ans = [intervals[0]]
        for interval in intervals:
            s1, e1, s2, e2 = ans[-1][0], ans[-1][1], interval[0], interval[1]
            if s2 <= e1:
                ans.pop()
                ans.append([s1, max(e1, e2)])
            else:
                ans.append(interval)
        return ans
