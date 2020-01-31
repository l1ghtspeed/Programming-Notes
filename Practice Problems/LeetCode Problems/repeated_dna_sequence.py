class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 11:
            return []
        solutions = set()
        seen = set()
        for i in range(10, len(s)+1):
            seq = s[i-10:i]
            if seq in seen and seq not in solutions:
                solutions.add(seq)
            elif seq not in seen:
                seen.add(seq)
        return solutions
        
