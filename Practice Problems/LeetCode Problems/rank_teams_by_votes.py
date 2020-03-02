import heapq

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        d = {}
        for vote in votes:
            for j in range(len(vote)):
                letter = vote[j]
                if letter not in d: 
                    d[letter] = [0 for p in range(len(votes[0]))]
                d[letter][j] += 1
        q = []
        for key in d:
            s = ''
            for n in d[key]:
                if n == 1000:
                    s += str(n)
                elif n >= 100:
                    s += '0'+str(n)
                elif n >= 10:
                    s += '00'+str(n)
                else:
                    s += '000' + str(n)
            val = int(s)*1000 + (300 - ord(key))
            heapq.heappush(q, (-1*val, key))
        ans = ''
        while q:
            n = heapq.heappop(q)
            ans += n[1]
        return ans
