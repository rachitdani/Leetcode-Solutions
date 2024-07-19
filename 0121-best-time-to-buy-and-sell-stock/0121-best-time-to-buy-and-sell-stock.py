class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i] < minn:
                minn = prices[i]
            
            curr_profit = prices[i] - minn

            if curr_profit > max_profit:
                max_profit = curr_profit


        return max_profit
            


            

        