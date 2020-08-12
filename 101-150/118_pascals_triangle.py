"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 记录输出
        output = []
        for i in range(1, numRows + 1):
            # 初始化每一行
            tmp = [1] * i
            # 借助杨辉三角的特性计算这一行的数字
            for j in range(1, i - 1):
                tmp[j] = output[i - 2][j - 1] + output[i - 2][j]
            # 把这一行添加到输出中去
            output.append(tmp)
        return output
"""
思路：动态规划算法，利用杨辉三角的特性，用上一行来计算当前行。算法时间复杂度为O(n^2)，空间复杂度也为O(n^2)，其中n为numRows，即为杨辉三角的行数。
"""
