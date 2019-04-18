class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (len(nums1) < len(nums2)):
            a = nums1
            n = len(nums1)
            b = nums2
            m = len(nums2)
        else:
            a = nums2
            n = len(nums2)
            b = nums1
            m = len(nums1)
            
        min_index = 0
        max_index = n 
        while (min_index <= max_index): 
            i = (min_index + max_index) // 2
            j = ((n + m + 1) // 2) - i 
            if (i < n and j > 0 and b[j - 1] > a[i]):      
                min_index = i + 1  
            elif (i > 0 and j < m and b[j] < a[i - 1]):      
                max_index = i - 1  
            else:
                if (i == 0):  
                    return float(b[j - 1])
                if (j == 0):  
                    return float(a[i - 1])          
                else: 
                    return float((a[i - 1]+b[j - 1])/2)