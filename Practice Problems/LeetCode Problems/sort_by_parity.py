class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even, odd = [], []
        for elem in A:
            if elem%2 == 0:
                even.append(elem)
            else:
                odd.append(elem)
        return even+odd
