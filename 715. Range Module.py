class RangeModule:

    def __init__(self):
        self.track = []        

    def addRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect(self.track, right)
        sub = []
        if start % 2 == 0:
            sub.append(left)
        if end % 2 == 0:
            sub.append(right)
        self.track[start:end] = sub

    def queryRange(self, left: int, right: int) -> bool:
        start = bisect.bisect(self.track, left)
        end = bisect.bisect_left(self.track, right)
        return start == end and start % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect(self.track, right)
        sub = []
        if start % 2:
            sub.append(left)
        if end % 2:
            sub.append(right)
        self.track[start:end] = sub
