class MyCalendarTwo:
    def __init__(self):
        self.calendar = {}

    def book(self, start: int, end: int) -> bool:
        if start not in self.calendar:
            self.calendar[start] = []
        if end not in self.calendar:
            self.calendar[end] = []
        self.calendar[start].append(1)
        self.calendar[end].append(-1)
        count = 0
        for key in sorted(self.calendar):
            for event in self.calendar[key]:
                count += event
            if key >= start and key <= end and count >= 3:
                self.calendar[start].pop()
                self.calendar[end].pop()
                return False
        return True
