"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # personal intervals
        taken = []
        for i in intervals:
            if len(taken) == 0:
                taken.append((i.start, i.end))
            else:
                for t in taken:
                    print(i.start, t[0], i.end)
                    print(i.start, t[1], i.end)
                    if not (i.start >= t[1] or i.end <= t[0]):
                        return False
                taken.append((i.start, i.end))
        return True

