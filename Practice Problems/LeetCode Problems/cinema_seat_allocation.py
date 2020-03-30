class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        d = {}
        for seat in reservedSeats:
            r, c = seat[0], seat[1]
            if r not in d:
                d[r] = [True, True, True]
            if c == 2 or c == 3:
                d[r][0] = False
            if c == 4 or c == 5:
                d[r][1] = False
                d[r][0] = False
            if c == 6 or c == 7:
                d[r][1] = False
                d[r][2] = False
            if c == 8 or c == 9:
                d[r][2] = False
        ans = (n-len(d))*2
        for key in d:
            if d[key][0] and d[key][2]:
                ans += 2
            elif d[key][0] or d[key][1] or d[key][2]:
                ans += 1
        return ans
