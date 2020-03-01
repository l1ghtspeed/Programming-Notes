class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        n1, n2 = num + 1, num + 2
        l1, l2 = (n1-1, [1, n1]), (n2-1, [1, n2])
        for i in range(1, math.floor(math.sqrt(n1))+1):
            if n1%i == 0 and abs(n1//i - i) < l1[0]:
                l1 = (n1//i - i, [i, n1//i])
        for j in range(1, math.floor(math.sqrt(n2))+1):
            if n2%j == 0 and abs(n2//j - j) < l2[0]:
                l2 = (n2//j - j, [j, n2//j])
        if l1[0] > l2[0]:
            return l2[1]
        return l1[1]
