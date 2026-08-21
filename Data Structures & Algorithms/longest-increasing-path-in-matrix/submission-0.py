class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        input: 2d int arr (matrix)
        putput: int (length of longest strictly increasing path)
        - inputs ints are >= 0
        - Brute force: backtracking. try from every cell to find the longest inc path and keep track of the max
        - many repeated parts of the paths we need to check
        - at each cell, 4 direction choices 4^mn
        - DFS/BFS + caching past results
        dp[i][j] = longest inc path from this cell
        '''
        longest_path = dict()   # maps (i,j) -> longest increasing path starting from i,j
        def dfs(i, j):
            if (i,j) in longest_path:
                return longest_path[(i,j)]
            else:
                longest_path[(i, j)] = 1
                for row_dir, col_dir in [(1,0), (-1, 0), (0, -1), (0, 1)]:
                    new_row = i + row_dir
                    new_col = j + col_dir
                    if 0<=new_row<len(matrix) and 0 <= new_col < len(matrix[0]) and matrix[new_row][new_col] > matrix[i][j]:
                        longest_path[(i, j)] = max(longest_path[(i, j)], 1+dfs(new_row, new_col))
                return longest_path[(i,j)]
        max_path = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_path = max(max_path, dfs(i,j))
        return max_path


                        


        