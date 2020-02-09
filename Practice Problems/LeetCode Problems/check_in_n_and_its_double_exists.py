class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for i in arr:
            if i in s:
                return True
            s.add(i*2)
            if i % 2 != 1:
                s.add(i//2)
        return False
        
