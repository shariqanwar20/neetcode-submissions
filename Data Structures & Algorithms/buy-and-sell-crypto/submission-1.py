class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l = 0
        for r in range(len(prices)):
            res = max(res, prices[r] - prices[l], 0)
            if prices[r] < prices[l]:
                l = r
            
        return res