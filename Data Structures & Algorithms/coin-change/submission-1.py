import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        unbounded knapsack
        min_coins[i][j] = min coins needed to make amount j using the first i coins
        min_coins[i][j] = min(min_coins[i-1][j], min_coins[i][j-coins[i-1]]) 
        # either don't/stop using current coin or continue using current coin
        '''
        min_coins = [math.inf for _ in range(amount+1)]
        for i in range(len(coins)+1):
            for j in range(amount+1):
                if j == 0:
                    min_coins[j] = 0
                elif i == 0:
                    min_coins[j] = math.inf
                else:
                    min_coins[j] = min_coins[j]
                    if j - coins[i-1] >= 0:
                        min_coins[j] = min(min_coins[j], 1+min_coins[j-coins[i-1]])
        if min_coins[amount] == math.inf:
            return -1
        return min_coins[amount]

                
