from collections import deque
import math
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        input: mxn 2d list of integers
        output: Nothing
        - modify the grid in place
        - -1 = obstacle
        - 0 = treasure chest (goal states)
        - INF = land cell
        replace the INF with the shortest distance to each treasure chest
        - If it cannot be reached, then do nothing.
        Q: We assume that the grid is surrounded by water?
        Q: 3000 < n*m < 10^6 => O(nm)/O(nmlognm)
        Multisource BFS from each treasure chest
        set -> visited cells
        queue, initially store all treasure chest cells (cell, dist from the treasure chest)
        '''
        # find all the treasure chest locations
        treasure_chests = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):   # assuming grid is rect
                if grid[i][j] == 0:
                    treasure_chests.append((i, j, 0))
        q = deque(treasure_chests)   # (row, col, dist from nearest chest)
        visited = set() # contains all cells we have processed (or modified cell value for)
        while q:
            row, col, dist_from_chest = q.popleft()
            if (row, col) in visited:
                continue
            # this is the first time we reach this cell, so update its dist
            visited.add((row, col))
            grid[row][col] = dist_from_chest
            # add its neighbors
            for row_dir, col_dir in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_row = row + row_dir
                new_col = col + col_dir
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] != -1 and grid[new_row][new_col] != 0:
                    q.append((new_row, new_col, dist_from_chest+1))
        


        
        