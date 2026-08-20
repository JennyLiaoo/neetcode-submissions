from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        input: 2d list of integers (grid)
        output: int (min num of minutes until there are no fresh fruit)
        Q: is it guaranteed that all fresh fruit can be reached from rotten? No -> -1
        Q: is the grid rectangular?
        Q: is there bounds to the size of the grid? 20 < nm < 3000 => O(nm^2)
        Q: once a fresh fruit turns rotten it stays rotten?
        Min number of minutes for all to become rotten = longest shortest path from a rotten orange to a fresh orange
        Multisource BFS from rotten oranges will give shortest path to all fresh oranges. We take the longest one as our output
        Can use some sort of counter to see if the amount of fresh oranges we found == total


        - 0 = empty, 1 = fresh, 2 = rotten
        '''
        rotten_oranges = [] 
        num_fresh = 0
        # find all rotten oranges
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten_oranges.append((i, j, 0))
                elif grid[i][j] == 1:
                    num_fresh += 1
        q = deque(rotten_oranges) # row, col, distance from nearest rotten orange = number of minutes it takes until this orange turns rotten
        max_minutes = 0
        num_fresh_reached = 0
        seen = set()    # set of all the visited cells
        while q:
            row, col, dist_from_rotten = q.popleft()
            if (row, col) in seen:
                continue
            seen.add((row, col))
            if grid[row][col] == 1:
                num_fresh_reached += 1
                max_minutes = max(max_minutes, dist_from_rotten)
            for row_dir, col_dir in [(1,0), (-1,0), (0, 1), (0, -1)]:
                new_row = row + row_dir
                new_col = col + col_dir
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                    q.append((new_row, new_col, dist_from_rotten+1))


        if num_fresh == num_fresh_reached:
            return max_minutes
        else:
            return -1




        