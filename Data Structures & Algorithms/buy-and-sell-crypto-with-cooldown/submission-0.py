class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        sequential one pass dp question
        input: list int (prices of neetcoin each day)
        output: max profit u can get from buying/selling stovk

        Constraints:
        - can only hold one coin at a time
        - cooldown of one day after selling
        - can complete inf transactions

        Q: do u start with a coin or no?
        Q: all values in prices is positive?
        Q; possibility of the best profit being not buying at all
        Q: one day period => u can sell _ buy
        Q: bound on length of prices? O(n)/O(nlogn)
        
        Algos:
        - greedy? if no cooldown, we could greedily just buy/sell for every increase
        - with cooldown, we need to consider more choices (i.e if i buy on this day, what if i miss a better opportunity on the next day?)
        - dp: choose to buy and sell or choose not to buy and sell 
        max_profit[i] = max profit obtainiable from buying and selling within the first i days
        max_profit[n] = answer
        max_profit[0] = 0
        max_profit[i] =  max(max_profit[i-1], for 2 <= j < i-1 s.t prices[j]<prices[i-1]: prices[i-1] - prices[j] + max_profit[j-1])
        # choose to sell today or not
        '''
        dp = [0] * (len(prices) + 1)

        for i in range(1, len(prices) + 1):
            # don't sell on day i-1
            dp[i] = dp[i - 1]

            # sell on day i-1
            for j in range(i - 1):
                previous_profit = dp[j - 1] if j >= 1 else 0

                dp[i] = max(
                    dp[i],
                    previous_profit + prices[i - 1] - prices[j]
                )

        return dp[len(prices)]
        
        
        