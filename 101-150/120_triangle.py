"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # 动态规划算法
        # 直接在给定的三角形数组上进行状态转移
        for i in range(1, len(triangle)):
            # 状态转移方程
            triangle[i][0] += triangle[i - 1][0]
            triangle[i][-1] += triangle[i - 1][-1]
            for j in range(1, i):
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        return min(triangle[-1])
               
"""
思路：采用动态规划算法，算法时间复杂度为O(n^2)，其中n为三角形的行数。由于我们直接在给定的三角形数组上进行状态转移，不使用额外的空间。因此算法空间复杂度为O(1)。如果遇到不能够修改原来给定的
三角形数组的要求，那么算法空间复杂度应该为O(n)，我们只需要用一个n维数组来储存即可。
"""
