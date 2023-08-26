class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start times.
        intervals.sort(key=lambda x: x[0])
        
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i-1][1]:
                if intervals[i][1] > intervals[i-1][1]:
                    intervals[i-1][1] = intervals[i][1]
                del intervals[i]
            else:
                i += 1
                
        return intervals
