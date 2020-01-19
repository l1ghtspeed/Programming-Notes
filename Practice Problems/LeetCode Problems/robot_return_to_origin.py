class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = { "L": 0, "R": 0, "U": 0, "D": 0 }
        for move in moves:
            d[move] += 1
        if d["L"] == d["R"] and d["U"] == d["D"]:
            return True
        return False
