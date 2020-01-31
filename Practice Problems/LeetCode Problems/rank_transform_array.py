class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        arr_sorted = sorted(arr)
        d = {}
        d[arr_sorted[0]] = 1
        for i in range(1, len(arr_sorted)):
            if arr_sorted[i] not in d:
                d[arr_sorted[i]] = d[arr_sorted[i-1]] + 1
        for i in range(len(arr)):
            arr[i] = d[arr[i]]
        return arr
                
