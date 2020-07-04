"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the 
diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
Note: m and n will be at most 100.
Example 1:
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # 存储网格的长与宽
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # 如果左上角有障碍，则直接返回0
        if obstacleGrid[0][0] == 1:
            return 0
        # 将左上角那一格的路径数设为1（因为前面判定过是否有障碍）
        obstacleGrid[0][0] = 1
        # 边界的初始化
        # 对于上边，若这一格没有障碍，且左边一格路径数为1（即之前都无障碍），则将这一格的路径数设为1
        for i in range(1,n):
            obstacleGrid[0][i] = int(obstacleGrid[0][i] == 0 and obstacleGrid[0][i - 1] == 1)
        # 对于左边，若这一格没有障碍，且上边一格路径数为1（即之前都无障碍），则将这一格的路径数设为1
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1)   
        # 对于右下方(m-1)*(n-1)的网格，每一格的路径数等于它左边格子的路径数加上它上边格子的路径数（如果没有障碍），否则直接为0。
        for i in range(1,m):
            for j in range(1,n):
                obstacleGrid[i][j] = (obstacleGrid[i][j - 1] + obstacleGrid[i - 1][j]) * (1 - obstacleGrid[i][j])
        return obstacleGrid[m - 1][n - 1]
 """
 思路：利用动态规划的方法，边界的初始化需要重新设定。其他思路与之前大致相同，只是多了一个障碍的判定。由于obstacleGrid的存在，因此不需要额外的空间，即空间复杂度为O(1)。
 """
