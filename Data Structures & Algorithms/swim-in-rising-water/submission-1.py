import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
        input: 2d int matrix 
        output: min time needed to reach bottom right square

        - each elem of grid is the elevation at that point
        - At time t, the water level is t
        - you can swim to an adjacent cell as long as its elevation <= t
        - Essentially finding a path from (0,0) to (n-1, m-1) where the maximum value along that path is minimized

        Q: at a single point in time, can u only take one step or can u take infinite number of steps as long as the water allows u to keep going
        Q: 

        Brute force:
        - backtracking through all paths to n-1, n-1 and find the path with the smallest largest value along its path.

        Optimization:
        - dijkstra's except the cost is the maximum element in the path? 
        - we greedily try to take the next path that has the minimum max path element
        - i.e each cell is a node, the edges connect adjacent cells, and the overall "cost" of the path is the largest number in that path
        - make sure to keep a set of cells that u already know the min cost of getting to it?

        Prove to urself that it works bro:
        - in dijktra the first time an elem is popped off a heap is its best cost for path to it
        - This is true in this case too because if there were a lower numbered path to this node from some other path, it wouldve been popped off first. if that path is not yet on the heap, it wouldve been added first cuz that path has smaller value than the current path
        - imagine u have some other path that reaches this node with smaller largest val (but ig not in heap yet)
            - there must be some part of that path explored/unexplired
            -since smaller, it must be that the val at any point of that path was smaller, so it shouldve been explored first and popped off first

        - dijkstra needs heap, seen set. finds min costing path from source to all other nodes
        -
        Q: start as val 0 at (0,0)?

        '''
        min_max_on_path = [[grid[0][0],0,0]]      # [max value on path, row, col]
        found = set()   # (row, col) of found min max paths for that cell
        while min_max_on_path:
            min_max, row, col = heapq.heappop(min_max_on_path)
            if (row, col) in found:
                continue
            elif (row, col) == (len(grid)-1, len(grid[0])-1):
                return min_max
            found.add((row, col))
            for row_dir, col_dir in [(0,1), (0,-1), (1,0), (-1,0)]:
                new_row = row+row_dir
                new_col = col+col_dir
                if 0<=new_row<len(grid) and 0<=new_col < len(grid[0]) and (new_row, new_col) not in found:
                    heapq.heappush(min_max_on_path, [max(grid[new_row][new_col], min_max),new_row,new_col])

        


        