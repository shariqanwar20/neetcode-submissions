"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x:(x.start, x.end))
        
        active = []
        res = 0
        for interval in intervals:
            while active and active[0] <= interval.start:
                heapq.heappop(active)
            
            heapq.heappush(active, interval.end)
            
            if len(active) > res:
                res = len(active)
        return res


        