class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mappings = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        n1, n2, num1, num2 = 0, 0, num1[::-1], num2[::-1]
        for i, char in enumerate(num1):
            n1 += (mappings[char] * (10 ** i))
        for i, char in enumerate(num2):
            n2 += (mappings[char] * (10 ** i))
        
        return str(n1 * n2)
