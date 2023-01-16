class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        ni = newInterval
        for i, ci in enumerate(intervals):
            if ni[0] < ci[0] and ni[1] < ci[0]:
                intervals.insert(i, ni)
                return intervals
            elif ni[0] <= ci[0] and ni[1] <= ci[1]:
                ci[0] = ni[0]
                return intervals  
            elif ni[0] >= ci[0] and ni[1] <= ci[1]:
                return intervals
            elif (ni[0] >= ci[0] and ni[0] <= ci[1]) or (ni[0] <= ci[0] and ni[1] >= ci[1]):
                if ni[0] < ci[0]:
                    ci[0] = ni[0]
                ci[1] = ni[1]
                # Merge overlaps.
                j = i+1
                while j < len(intervals):
                    cj = intervals[j]
                    if ci[1] < cj[0]:
                        return intervals
                    elif ci[1] >= cj[0] and ci[1] <= cj[1]:
                        ci[1] = cj[1]
                        print(cj, ci)
                        del intervals[j]
                        return intervals
                    else:
                        del intervals[j]
                return intervals

        intervals.append(ni)
        return intervals


