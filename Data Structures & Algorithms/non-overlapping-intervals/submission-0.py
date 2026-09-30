class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0], -x[1]))

        count = 0
        prev = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < prev:
                count += 1
                prev = min(prev, end)
            else:
                prev = end
        return count