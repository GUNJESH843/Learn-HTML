class MyCalendarTwo:

    def __init__(self):
        self.event = []
        self.overlap = []

    def book(self, start: int, end: int) -> bool:
        for e, s in self.overlap:
            if not(start >= s or end <= e ):
                return False
        for s,e in self.event:
            if not (end <= s or start >= e):
                self.overlap.append((max(start,s),min(e, end)))
        self.event.append((start, end))
        return True
    