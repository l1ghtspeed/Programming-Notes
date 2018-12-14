'''
Problem Description:

This question was asked by Riot Games.

Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:

record(timestamp): records a hit that happened at timestamp
total(): returns the total number of hits recorded
range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)

'''

class HitCounter:
    def __init__(self):
        self.timestamps = []

    def record(self, timestamp):
        self.timestamps.append(timestamp)
    
    def total(self):
        return len(self.timestamps)
    
    def range(self, lower, upper):
        count = 0
        for timestamp in self.timestamps:
            if timestamp >= lower and timestamp <= lower:
                count+=1
        return count
    