class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        '''
        input: int list (piles)
        output: bool (true if Alice wins)

        - even number of piles, each with pile[i] stones
        -total num stones are odd
        - end with most stones
        - take pile from beginning or from end
        - whoever has most stones win

        At each point in time there are two choices, take from front or back
        there are repeated subproblems too (i.e alice take from front, bob take from back and bob take from front alice take from back leaves us with the same remianing piles to look at)

        dp[i][j] = max amount obtainable from taking piles i to j. 
        dp[i][j] = max(piles[i] - dp[i-1][j] + max(dp[i-2][j], dp[i-1][j+1]), piles[j] +)
        - if taking piles[i] is the better choice, the other person will take max dp[i-1][j], so either i-1 or j. in which case, the space turns into either dp[i-2][j] or dp[i-1][j+1]. 

        dp[i][j] = max score advantage player whose turn it is can guarantee using piles i to j
        = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        -> dp[i+1][j] = opponent remaining score - ur remaining score
        piles[i] - opponent score + ur rem score = ur score - opp score. if > 0 => win
        '''
        dp = [[0 for _ in range(len(piles))] for _ in range(len(piles))]
        for i in range(len(piles)-1,-1,-1):
            for j in range(i,len(piles)):
                if i == j:
                    dp[i][j] = piles[i]
                else:
                    dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        return dp[0][len(piles)-1] > 0

        