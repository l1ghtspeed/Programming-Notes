# Q14

import math

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        target = str(x)
        for i in range(len(target)//2):
            if target[i] != target[-1*(i+1)]:
                return False
        return True
        

    def isPalindromeInt(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0 or x == 1:
            return True
        elif (x < 0):
            return False
        newNum = 0
        temp = x
        order = int(math.ceil(math.log10(x)))
        for i in range(0, order):
            div = (temp//(10**(order-i-1)))
            toAdd = div * (10**i)
            newNum += toAdd
            temp -= div * (10**(order-i-1))

        if newNum == x:
            return True
        
        return False

s = Solution()
print(s.isPalindromeInt(121121))
