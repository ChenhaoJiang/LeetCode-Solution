"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
Example:
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""
def largestRectangleArea(heights):
    stack = []
    max_area = 0
    for i in range(len(heights)):
        while len(stack) > 0 and heights[i] < heights[stack[-1]]:
            prev = stack.pop()
            if len(stack) > 0:
                max_area = max(max_area, (i - stack[-1] - 1) * heights[prev])
            else:
                max_area = max(max_area, i * heights[prev])
        stack.append(i)
    while len(stack) > 0:
        prev = stack.pop()
        if len(stack) > 0:
            max_area = max(max_area, (len(heights) - stack[-1] - 1) * heights[prev])
        else:
            max_area = max(max_area, len(heights) * heights[prev])
    return max_area
    
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 考虑特殊情况，即矩阵长或宽为0
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        heights = [0] * len(matrix[0])
        max_area = 0
        # 分层遍历，每一次遍历将heights矩阵传入largestRectangleArea()函数
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] += 1
            max_area = max(max_area, largestRectangleArea(heights))
        return max_area
 """
 思路：在84题的基础上进行修改，采用分层遍历，每一次遍历将heights矩阵传入largestRectangleArea()函数。
 """
