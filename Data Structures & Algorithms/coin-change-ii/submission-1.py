class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        Unbounded knapsack
        -input: int array (coins), int (target)
        -output: int (number distinct combination that make up total amount)

        - combinations => order doesn't matter but that means order does matter for us lol

        Q: unbounded?
        Q: is coins unique?
        Q: is amount + coins positive?
        Q: bounds on 
        num_ways[i][j] = num ways to make a sum of j using the first i coins
        num_ways[i][j] = if j >= nums[i-1]: num_ways[i-1][j] + num_ways[i][j-nums[i-1]]
        num_ways[0][j] = 0
        num_ways[i][0] = 1
        num_ways[0][0] = 1
        reduce space complexity iterate forwards ciz  relies on current row smaller values already being calculated
        '''

        num_ways = [0 for i in range(amount+1)]
        for i in range(len(coins)+1):
            for j in range(amount+1):
                if j == 0:
                    num_ways[j] = 1
                elif i == 0:
                    num_ways[j] = 0
                else:
                    num_ways[j] = num_ways[j]
                    if j >= coins[i-1]:
                        num_ways[j] += num_ways[j-coins[i-1]]
        return num_ways[amount]
                    



        