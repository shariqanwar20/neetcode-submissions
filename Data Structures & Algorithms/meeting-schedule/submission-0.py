"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x : x.start)
        def is_overlap(a, b):
            return b.start < a.end

        for i in range(1, len(intervals)):
            if is_overlap(intervals[i-1], intervals[i]):
                return False
        return True