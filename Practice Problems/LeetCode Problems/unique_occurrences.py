class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        s = set()
        for key in d:
            if d[key] in s:
                return False
            s.add(d[key])
        return True
