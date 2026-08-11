class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans=0
        for i in range(1, len(prices)):
            buy = min(prices[:i])
            ans = max(ans, prices[i]-buy)
        
        return ans