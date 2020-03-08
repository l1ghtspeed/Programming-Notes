class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff, d = sys.maxsize, {}
        for i in range(len(arr)-1):
            diff = abs(arr[i] - arr[i+1])
            if diff not in d:
                d[diff] = []
            d[diff].append([arr[i], arr[i+1]])
            min_diff = min(min_diff, diff)
            
        return d[min_diff]
            
