class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s = []
        count = 0
        for i in range(len(height)):
            if height[i] != 0:
                lowestH = 0
                while s and (s[-1][0] <= height[i]):
                    count += (s[-1][0]-lowestH)*(i - s[-1][1] - 1)
                    if lowestH < s[-1][0]:
                        lowestH = s[-1][0]
                    s.pop()
                if s:
                    count += (height[i] - lowestH) * (i - s[-1][1] - 1)
                s.append((height[i], i))
            
        return count
