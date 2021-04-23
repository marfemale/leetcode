class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = inf, 0
        for price in prices:
            buy = min(price, buy)
            profit = max(profit, price - buy)
        return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0
        prices += [0]
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                res += prices[i - 1] - buy
                buy = prices[i]
        return res
      
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [-inf, 0, -inf, 0]#buy1, sell1, buy2, sell2
        for price in prices:
            dp[0] = max(dp[0], -price)
            dp[1] = max(dp[1], price + dp[0])
            dp[2] = max(dp[2], dp[1] - price)
            dp[3] = max(dp[3], dp[2] + price)
        return max(dp[1], dp[3])

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not k:
            return 0
        dp = [-inf, 0] * k
        for price in prices:
            dp[0] = max(dp[0], -price)
            dp[1] = max(dp[1], dp[0] + price)
            for i in range(1, k):
                dp[i * 2] = max(dp[i * 2], dp[i * 2 - 1] - price)
                dp[i * 2 + 1] = max(dp[i * 2 + 1], dp[i * 2] + price)
        return max(dp)
