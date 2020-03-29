class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if bill == 10 and d[5] > 0:
                d[5] -= 1
            elif bill == 10:
                return False
            if bill == 20 and (d[5] > 2 or (d[5] > 0 and d[10] > 0)):
                if d[10] > 0:
                    d[10] -= 1
                    d[5] -= 1
                else:
                    d[5] -= 3
            elif bill == 20:
                return False
            d[bill] += 1
        return True
                    
