class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        elem_count = {}
        for elem in arr:
            if elem not in elem_count:
                elem_count[elem] = 0
            elem_count[elem] += 1
        l, ans, count = len(arr), 0, 0
        for elem in sorted(elem_count, elem_count.get, reverse=True):
            ans += 1
            count += elem
            if count >= l/2:
                break
        return ans
