"""
Say you have an array for which the i-th element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most k transactions.
Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
Example 1:
Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:
Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        
        # 方法一：贪心算法
        if k == 0 or not prices:
            return 0
        n = len(prices)
        if k >= n//2:
            maxprofit = 0
            for i in range(1, len(prices)):
                # 仅当股价上升时，才计算收益
                if prices[i] > prices[i - 1]:
                    maxprofit += prices[i] - prices[i - 1]
            return maxprofit
        else:
            buy = [float("inf")] * k
            profit = [0] * k 
            for price in prices:
                buy[0] = min(buy[0], price)
                profit[0] = max(profit[0], price - buy[0])
                # 相当于用前一次的收益抵消掉部分后一次的购买价格
                for i in range(1, k):
                    buy[i] = min(buy[i], price - profit[i - 1])
                    profit[i] = max(profit[i], price - buy[i])
            return profit[-1]
        
        """
        # 方法二：动态规划算法
        if not prices:
            return 0
        n = len(prices)
        # 由于同天买卖对利润不会产生影响，因此有效的交易由买入和卖出构成，则至少需要两天。
        # 当k大于等于n//2时，相当于无交易次数限制。
        if k >= n//2:
            #dp的初始化，dp[][]，这里dp有两个框，第一个表示天数，第二个表示是否持有股票，0不持有，1持有
            dp = [[0,0] for _ in range(n)]
            #第0天不持有利润为0 
            dp[0][0] = 0    
            #第0天持有股票利润为负的第0天股票价格，也就是买入
            dp[0][1] = -prices[0] 
            for i in range(1,n):   
                #第i天不持股的最大利润，可能是第i-1天不持股的最大利润或者第i-1天持股然后在第i天卖出
                #第i天持股的最大利润，可能是第i-1天持股的最大利润或者第i-1天不持股然后在第i天买入
                dp[i][0] = max(dp[i - 1][0],dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1],dp[i - 1][0] - prices[i])
            return dp[-1][0]   #最后返回最后一天不持股的利润
        else:
            #对dp初始化，这里是三维的列表，举个例子[[[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0]]]
            dp = [[[0,0] for _ in range(k + 1)] for _ in range(n)]  
            for i in range(1, n):
                #第i天0笔交易不持股的利润为0
                #第i天0笔交易持股是不可能，用利润负无穷表示这种不可能
                dp[i][0][0] = 0
                dp[i][0][1] = float("-inf")
            for j in range(1, k + 1):
                #第0天i笔交易不持股的利润为0
                #第0天i笔交易持股的利润为负的第0天股票价格，即在这一天买入股票
                dp[0][j][0] = 0
                dp[0][j][1] = -prices[0]

            for i in range(1,n):
                for j in range(1, k + 1):
                    # 第i天j笔买入不持股的最大利润，可能是i-1天j笔买入不持股的最大利润或者第i-1天j笔买入持股然后在第i天卖出
                    # 第二维参数记录的实际上是买入次数（如果是卖出次数或者交易次数，则需要稍微修改状态转移方程）
                    # 第i天j笔买入持股的最大利润，可能是i-1天j笔买入持股的最大利润或者第i-1天j笔买入不持股然后在第i天买入
                    dp[i][j][0] = max(dp[i - 1][j][0],dp[i - 1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i - 1][j][1],dp[i - 1][j - 1][0] - prices[i])
            #最后返回最后一天不持股且交易次数最多的利润
            return dp[-1][-1][0]
        """
"""
思路：方法一为贪心算法，有点类似于第123题的贪心算法，这里用一个k维数组来存储j次交易能获得的最大利润以及一个k维数组来存储每一次交易的最低价格，同时每次用前一次的收益抵消掉部分后一次的购买价格。但是
测试案例209为一个k极大的情况，这种情况下就会导致内存溢出，因此我们通过k >= n//2来进行判断。由于同天买卖对利润不会产生影响，因此有效的交易由买入和卖出构成，则至少需要两天。当k大于等于n//2时，相当
于无交易次数限制，这种情况则为122题的情况。算法时间复杂度为O(k*n)，空间复杂度为O(min{k,n})，视k与n的关系而定。方法二为动态规划算法，有点类似于第123题的动态规划算法，详见注释。同样地，这边通过
k >= n//2来进行判断，当k大于等于n//2时，相当于无交易次数限制，这种情况则为122题的情况。算法时间复杂度为O(k*n)，空间复杂度为O(k*n)，视k与n的关系而定。
"""
