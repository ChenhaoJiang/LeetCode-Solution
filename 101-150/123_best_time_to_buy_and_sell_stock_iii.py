def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        # 方法一：贪心算法
        buy_1 = buy_2 = float("inf")
        profit_1 = profit_2 = 0
        for price in prices:
            buy_1 = min(buy_1, price)
            profit_1 = max(profit_1, price - buy_1)
            # 相当于用第一次的收益抵消掉部分第二次的购买价格
            buy_2 = min(buy_2, price - profit_1)
            profit_2 = max(profit_2, price - buy_2)
        return profit_2
        """
        # 方法二：动态规划算法
        if not prices:
            return 0 
        # 初始化三维DP Table
        dp = [[[0, 0] for _ in range(3)] for _ in range(len(prices))] 
        for i in range(1, len(prices)): 
            # 没有买入过股票，且手头没有持股，则获取的利润为0
            dp[i][0][0] = 0 
            # 没有买入过股票，不可能持股，用利润负无穷表示这种不可能   
            dp[i][0][1] = float("-inf") 

        # 前面k = 0已经赋值了，这里k从1开始
        for i in range(1, 3): 
            # 第0天i笔交易但不持股，利润为0
            dp[0][i][0] = 0   
            # 第0天i笔交易持股，利润为负的第0天股票价格
            dp[0][i][1] = -prices[0]  
        # 当买入时算一次交易
        # 状态转移方程如下：
        for i in range(1,len(prices)):
            for k in range(1,3):
                dp[i][k][0] = max(dp[i - 1][k][1] + prices[i], dp[i - 1][k][0])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[-1][-1][0]
"""
思路：方法一为贪心算法，与121题的贪心算法比较类似，只是多了一次交易，通过用第一次的收益抵消掉部分第二次的购买价格即可实现。算法时间复杂度为O(n)，空间复杂度为O(1)。方法二为动态规划，状态转移方程为：
dp[i][k][0] = max(dp[i - 1][k][1] + prices[i], dp[i - 1][k][0])     # 右边:今天卖了昨天持有的股票，所以两天买入股票的次数都是j
dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i]) # 右边:昨天没有持股而今天买入一只，故昨天买入的次数是j-1
其中dp[i][k][0]表示第i天交易k次不持有股票的最大利润，dp[i][k][0]表示第i天交易k次持有股票的最大利润。该算法时间复杂度为O(n), 空间复杂度也为O(n)。
"""
