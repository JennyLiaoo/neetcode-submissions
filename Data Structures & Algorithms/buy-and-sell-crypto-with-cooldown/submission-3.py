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
        0 to i-1
        0 to i-2
        remembe to include not selling on day i. max_profit[i] = price gained from selling on day i and buying on day j + price gained from buying and selling before from days 0 to j-2 (first j-1 days)
        '''

        '''
        hold[i] = max profit if I'm HOLDING a stock after day i
        sold[i] = max profit if I SOLD a stock on day i
        rest[i] = max profit if I'm NOT holding and did NOT sell today

        j = buying (not holding anything, can either choose to buy or do nothing) or selling (holding smt. can choose to continue holding or do nothing)
        max_profit[i][j] = max profit gainable by day i if u r currently in a buy or sell state
        max_profit[i][j] = max(max_profit[i-1][j] (holding), 
            if j = buying: prices[i] + max_profit[][]
            if j = selling: max_profit[][]

        dp[i][0] = max profit by end of day i if not holding (previously not holding, now not holding or previously sold and now not holding)
        dp[i][1] = max profit by day i if i am holding (previously was holding, now am holding. or previously not holding for more thn cooldown and bought today and now am holding)
        '''
        max_profit = [[0 for _ in range(2)] for _ in range(len(prices))]

        # day 0
        max_profit[0][0] = 0
        max_profit[0][1] = -prices[0]

        for i in range(1, len(prices)):
            # not holding today:
            # either weren't holding yesterday,
            # or sell the stock we held yesterday
            max_profit[i][0] = max(
                max_profit[i-1][0],
                max_profit[i-1][1] + prices[i]
            )

            # holding today:
            # either keep holding,
            # or buy today
            previous_profit = max_profit[i-2][0] if i >= 2 else 0

            max_profit[i][1] = max(
                max_profit[i-1][1],
                previous_profit - prices[i]
            )

        return max_profit[len(prices)-1][0]



                
                
                