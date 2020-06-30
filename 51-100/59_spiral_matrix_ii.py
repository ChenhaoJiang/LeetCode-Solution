"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.
Example:
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        #初始化矩阵
        matrix = [[0] * n for _ in range(n)]
        # 分别定义了四个边界
        left, right, top, bottom = 0, n-1, 0, n-1
        # 走完n^2步就结束
        len_path = 1
        while len_path <= n ** 2:
            # 向右
            for i in range(left, right + 1):
                matrix[top][i] = len_path
                len_path += 1
            # 向下
            for i in range(top + 1, bottom + 1):
                matrix[i][right] = len_path
                len_path += 1
            # 向左
            for i in range(right - 1, left - 1, -1):
                matrix[bottom][i] = len_path
                len_path += 1
            #向上
            for i in range(bottom - 1, top, -1):
                matrix[i][left] = len_path
                len_path += 1
            # 更新边界
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return matrix
"""
思路：有点像第一次的螺旋矩阵，这次用了稍微不一样的方法，不再用一个矩阵来记录该点是否已访问，而是靠四个边界来约束路径。
"""
