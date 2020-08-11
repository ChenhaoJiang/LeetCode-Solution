"""
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        """
        # 方法一：动态规划
        # dp[i] 表示前 i 天的最大利润，因为我们始终要使利润最大化，则：
        # dp[i] = max(dp[i-1], prices[i]-minPrice), 其中minPrice为前i天的最低股价
        
        # 判断边界条件
        if not prices:
            return 0 
        minPrice = prices[0]
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            minPrice = min(prices[i], minPrice)
            dp[i] = max(dp[i - 1], prices[i] - minPrice)
        return dp[-1]
        """
        # 方法二：遍历一次prices数组（动态规划的演变）
        maxprofit = 0
        minPrice = float("inf")
        for price in prices:
            minPrice = min(price, minPrice)
            maxprofit = max(price - minPrice, maxprofit)
        return maxprofit
"""
思路：方法一为动态规划，dp[i] 表示前 i 天的最大利润，因为我们始终要使利润最大化，则：dp[i] = max(dp[i-1], prices[i]-minPrice), 其中minPrice为前i天的最低股价。时间复杂度为O(n),
空间复杂度也为O(n)。方法二是动态规划的演变，区别在于不再用一个数组去存储前i天的最大利润，而是变为用一个变量去存储当前最大利润。时间复杂度为O(n)，空间复杂度为O(1)。
"""
