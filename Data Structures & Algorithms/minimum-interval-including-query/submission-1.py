class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        '''
        input: 2d int arr (intervals[]), int arr (queries) query[j]  length shortest interval i s.t i < queries[j] < i

        Q: inclusive? disjoint
        - preprocess
        - seg tree=>?
        - sweep line
        map query=>query,i, sort queries
        add int i into set, if in dict, can find len
        map intervals to single arr (val,i,s/e)
        when we've seen s, add to dict. when we find e, we 

        Sol: min heap by interval size
        map query->index, process in ascending order
        while top end < query, keep popping till we find valid. then use that
        if no valid, -1
        only have interval with start <= query in heap
        
        '''
        query_i = defaultdict(list)
        for i,query in enumerate(queries):
            query_i[query].append(i)

        queries.sort()
        interval_size = []  # min heap (size,i)
        intervals.sort()

        res = [-1 for _ in range(len(queries))]
        i = 0
        int_i = 0
        while i < len(queries):
            curr_query = queries[i]
            while int_i < len(intervals):
                if intervals[int_i][0] <= curr_query:
                    size = intervals[int_i][1] - intervals[int_i][0]+1
                    heapq.heappush(interval_size, (size, int_i))
                    int_i+=1
                else:
                    break

            while interval_size and intervals[interval_size[0][1]][1] < curr_query:
                heapq.heappop(interval_size)

            if interval_size:
                size, j = interval_size[0]
                
                query_index = query_i[curr_query][-1]
                query_i[curr_query].pop()
                res[query_index] = size
            i+= 1
        return res





        