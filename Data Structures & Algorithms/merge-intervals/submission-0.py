class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        input: array (intervals[i] = [start, end])
        output: array of non overlapping intervals

        - output any order
        - Q: end == start => overlapping
        - Q: well formed, can have 0 interval
        - Q: not necessairly sorted

        - sort intervals by start time
        - compare adjacent intervals
        '''
        intervals.sort()
        i = 0
        disjoint_intervals = []
        while i < len(intervals):
            if not disjoint_intervals:
                disjoint_intervals.append(intervals[i])
            else:
                prev_start, prev_end = disjoint_intervals[-1]
                curr_start, curr_end = intervals[i]
                if curr_start <= prev_end:
                    disjoint_intervals.pop()
                    new_interval = [prev_start, max(prev_end, curr_end)]
                    disjoint_intervals.append(new_interval)
                else:
                    disjoint_intervals.append(intervals[i])

            i+=1
        return disjoint_intervals



        