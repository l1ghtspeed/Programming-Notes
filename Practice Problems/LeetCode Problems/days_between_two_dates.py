from datetime import date
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = date(int(date1[:4]), int(date1[5:7]), int(date1[8:]))
        d2 = date(int(date2[:4]), int(date2[5:7]), int(date2[8:]))
        return abs((d2-d1).days) 
