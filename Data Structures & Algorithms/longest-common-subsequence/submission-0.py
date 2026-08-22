class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        input: two strings
        output: int (length of longest common subsequence)

        Q: does it necessairly exist?
        Q: clarify definition of subsequence
        Q: bounds of strings 

        BF: generate all subsequences of both and compare - backtracking, place in sets and do set intersection then take the longest one O(2^n) exponential solution

        generating subsequence is repetitve, and we reach the same state a lot

        maximizing DP

        max_common[i][j] = maximum common subsrquence between test1[:i] and text2[:j]
        max_common[i][j] = 
        max(
        - dont match the current chars max_common[i-1][j], max_common[i][j-1]
        - if text1[i-1] == text2[j-1] then have the choice to include 1+max_common[i-1][j-1]))
        max_common[0][0] = 0
        max_common[i][0] = 0
        max_common[len(text1)][len(text2)]

        cat, caat = 3
        [0,0,0,0,0]
        [0,1,0,0,0]
        [0,1,2,2,2]
        [0,1,2,2,3]

        '' abcd = 0
        [0,0,0,0,0]
        '''
        max_common = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        for i in range(1,len(text1)+1): #3
            for j in range(1,len(text2)+1): #4
                max_common[i][j] = max(max_common[i-1][j], max_common[i][j-1])
                if text1[i-1] == text2[j-1]:
                    max_common[i][j] = max(max_common[i][j], 1+max_common[i-1][j-1])

        return max_common[len(text1)][len(text2)]


        