class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        ans = []
        for i in range(lo, hi+1):
            num_steps = self.get_num_steps(i)
            ans.append((num_steps, i))
        ans.sort()
        return ans[k-1][1]
    
    def get_num_steps(self, num):
        count = 0
        while not math.log2(num).is_integer():
            if num%2 == 1:
                num = num*3 + 1
            else:
                num = num//2
            count += 1
        return count + int(math.log2(num))
