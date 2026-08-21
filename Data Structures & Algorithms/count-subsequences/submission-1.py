class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        input: strings s, t
        output: int (num of distinct subsequeneces of s which are equal to t)
        - 0/1 knapsack problem (choosing characters in s to be a part of a subsequence which must "sum to" t)
        Q: subsequence is not necessairly contiguous + same order right? 
        Q: consists of only english letters?
        Q: is t < s?
        Q: 1 < n, m <= 1000
        Brute force:
        - generate all subsequences of s and compare to t.
        - choose to incl/not incl for each char (2 choices per char) => O(2^n)
        - same repeated subproblems

        Counting DP problem
        num_ways[i][j] = number of distinct subsequences of s[:i] which are equal to t[:j]
        num_ways[i][j] = num_ways[i-1][j] + if s[i-1] == t[j-1]: + num_ways[i-1][j-1] 
        num_ways[0][0] = 1
        num_ways[i][0] = 1
        num_ways[0][j] = 0
        num_ways[s][t] = answer
        O(st)
        '''
        num_ways = [0 for _ in range(len(t)+1)]
        for i in range(len(s)+1):
            for j in range(len(t), -1, -1):
                if j == 0:
                    num_ways[j] = 1
                elif i == 0:
                    num_ways[j] = 0
                else:
                    num_ways[j] = num_ways[j]
                    if s[i-1] == t[j-1]:
                        num_ways[j] += num_ways[j-1]
        return num_ways[len(t)]

        