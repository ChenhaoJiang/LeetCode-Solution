"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 存储网格的长与宽
        m = len(grid)
        n = len(grid[0])
        # 采用动态规划，每一格到右下角的最小路径和等于该格的权值加上它下方或右方格子中最小路径和中较小的那一个。
        # 右边界的定义
        for i in range(m - 2, -1, -1):
            grid[i][n - 1] += grid[i + 1][n - 1]
        # 下边界的定义
        for i in range(n - 2, -1, -1):
            grid[m - 1][i] += grid[m - 1][i + 1]
        # 动态规划，求网格中其他格子到右下角的最小路径和
        for i in range (m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                grid[i][j] += min(grid[i + 1][j], grid[i][j + 1]) 
        return grid[0][0]
"""
思路：采用动态规划的方法，与62、63两题思路较为类似。时间复杂度为O(mn)，由于没有使用额外的储存空间，而是直接存储在了grid矩阵中，因此空间复杂度为O(1)。
"""
