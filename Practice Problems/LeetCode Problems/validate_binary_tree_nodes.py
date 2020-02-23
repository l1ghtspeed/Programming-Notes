class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        n1, n2 = 0, 0
        s1, s2 = set(), set()
        for i in range(n):
            if leftChild[i] in s2 or leftChild[i] in s1 or rightChild[i] in s1 or rightChild[i] in s2:
                return False
                
            if leftChild[i] not in s1 and leftChild[i] != -1:
                s1.add(leftChild[i])
                n1 += 1
            if rightChild[i] not in s2 and rightChild[i] != -1:
                s2.add(rightChild[i])
                n2 += 1
        if n1 + n2 != n-1:
            return False
        return True
