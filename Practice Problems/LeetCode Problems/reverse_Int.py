# Q7

import math
class Solution:
    
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        if x < 0:
            ret = int(str(abs(x))[::-1])*-1 
        else:
            ret = int(str(x)[::-1])
            
        if ret >= 2**31 or ret < -1*2**31:
            return 0
        else:
            return ret
        

s = Solution()
print(s.reverse(11))