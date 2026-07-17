class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx=0
        buy=prices[0]
        for i in range(len(prices)):
            if prices[i]>buy:
                mx=max(mx,prices[i]-buy)
            buy=min(buy,prices[i])
        return mx