class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        summ = sum(A)
        if summ % 3 != 0:
            return False
        num_partitions, count, target = 0, 0, summ/3
        for num in A:
            count += num
            if count == target:
                num_partitions += 1
                count = 0
        if num_partitions == 3 and count == 0:
            return True
        return False
