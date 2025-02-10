"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x: x.start)

        ivl = intervals[0]

        for i in range(1, len(intervals)):

            if(ivl.end > intervals[i].start):
                return False
            ivl = intervals[i]
        

        return True
