class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key = lambda x: x[1])
        
        newInterval = intervals[0]

        for i in range(1, len(intervals)):

            if(newInterval[1] > intervals[i][0]):
                res += 1
            else:
                newInterval = intervals[i]
        
        return res
