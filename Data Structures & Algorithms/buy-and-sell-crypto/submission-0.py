class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # for loop on list that each time find the largest item id
        profit = 0 
        for ind, price in enumerate(prices):
            sell = max(prices[ind::])
            profit = max(sell-price, profit)

        return profit


