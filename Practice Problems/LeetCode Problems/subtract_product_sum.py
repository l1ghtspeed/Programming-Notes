class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        if not n or n == 0:
            return 0
        
        s, summ, prod = str(n), 0, 1
        for digit in s:
            d = int(digit)
            prod *= d
            summ += d
        
        return prod-summ
