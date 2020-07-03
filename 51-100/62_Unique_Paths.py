"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the 
diagram below). How many possible unique paths are there?
Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:
Input: m = 7, n = 3
Output: 28
Constraints:
1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
"""

class Solution:
    def uniquePaths(self, m, n):
        """
        # 直接排列组合，因此最终走的路径都是固定的，都是向右走m-1步，然后向下走n-1步
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))
        # 由于要计算阶乘，因此这种方法效率并不是最高的
        """
        """
        # 动态规划
        # 因为只能向右或向下走，因此每一格的路径数等于它上面格子的路径数+左边格子的路径数
        # 生成一个m*n的矩阵，其中第一行和第一列全是1
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
        """
        # 动态规划算法的优化，降低了空间复杂度
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j-1]
            pre = cur[:]
        return pre[-1]
"""
思路：提供了三个版本的代码，思路详见注释。
"""
