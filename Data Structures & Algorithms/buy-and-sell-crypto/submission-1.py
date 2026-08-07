class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers problem
        # Points are not from two side but 

        l = 0
        r = 1
        max_=0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_= max(max_, profit)
            else: 
                l = r
            r+=1

        return max_

