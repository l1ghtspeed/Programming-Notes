class TweetCounts:

    def __init__(self):
        self.store = {} 

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.store:
            self.store[tweetName] = []
        self.store[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        m = 0
        
        if freq == "minute":
            m = 60
        elif freq == "hour":
            m = 3600
        elif freq == "day":
            m = 86400
        
        ans = [0 for _ in range(((endTime-startTime)//m)+1)]
        for i in self.store[tweetName]:
            res = (i-startTime)//m
            if res < len(ans) and i >= startTime and i <= endTime:
                ans[res] += 1
            else:
                break
        return ans
