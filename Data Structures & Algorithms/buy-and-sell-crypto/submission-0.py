class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force - check every possible 
        min_buy = prices[0]
        ans = 0
        for i in prices:
            ans = max(ans, i - min_buy)
            min_buy = min(min_buy, i)
        return ans

        