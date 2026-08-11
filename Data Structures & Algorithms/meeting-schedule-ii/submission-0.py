"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []
        for i in range(len(intervals)):
            starts.append(intervals[i].start)
            ends.append(intervals[i].end)

        starts.sort()
        ends.sort()

        s, e = 0, 0
        count = 0
        maxCount = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            maxCount = max(maxCount, count)
        return maxCount

