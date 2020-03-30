# this can be refactored to be cleaner
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        qset = set()
        for queen in queens:
            qset.add(tuple(queen))
        ans = []
        
        for i in range(king[0]-1, -1, -1):
            x, y = i, king[1]
            if (x, y) in qset:
                ans.append((x, y))
                break
        for i in range(king[0]+1, 8):
            x, y = i, king[1]
            if (x, y) in qset:
                ans.append((x, y))
                break
        for i in range(king[1]-1, -1, -1):
            x, y = king[0], i
            if (x, y) in qset:
                ans.append((x, y))
                break
        for i in range(king[1]+1, 8):
            x, y = king[0], i
            if (x, y) in qset:
                ans.append((x, y))
                break
        x, y = king[0]-1, king[1]-1
        while x >= 0 and y >= 0:
            if (x, y) in qset:
                ans.append((x, y))
                break
            x, y = x - 1, y - 1
        x, y = king[0] + 1, king[1] + 1
        while x < 8 and y < 8:
            if (x, y) in qset:
                ans.append((x, y))
                break
            x, y = x + 1, y + 1
        x, y = king[0] + 1, king[1] - 1
        while x < 8 and y >= 0:
            if (x, y) in qset:
                ans.append((x, y))
                break
            x, y = x + 1, y - 1
        x, y = king[0] - 1, king[1] + 1
        while x >= 0 and y < 8:
            if (x, y) in qset:
                ans.append((x, y))
                break
            x, y = x - 1, y + 1
        return ans
