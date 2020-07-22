"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
The largest rectangle is shown in the shaded area, which has area = 10 unit.
Example:
Input: [2,1,5,6,2,3]
Output: 10
"""

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 用一个栈去储存
        stack = []
        # 储存当前最大的面积
        max_area = 0
        # 遍历整个直方图（数组）
        for i in range(len(heights)):
            # 每次当新元素进栈时，将栈中所有比它小的元素弹出进行结算。（这样到最后能保证栈中元素是升序排列的）
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                # 弹出元素
                prev = stack.pop()
                # 右边界总归是当前进栈元素所在的位置
                # 如果弹出这个元素后，栈中还有别的元素，那说明对于这个元素来说左边界就是栈中前一个元素所在的位置（因为栈中前一个元素一定比它小）
                if len(stack) > 0:
                    max_area = max(max_area, (i - stack[-1] - 1) * heights[prev])
                # 如果这个元素是栈里最后一个元素，那说明左边界就是整个直方图的左边界
                else:
                    max_area = max(max_area, i * heights[prev])
            stack.append(i)
        # 将所有剩余的元素弹出栈进行结算，这些元素的右边界均为整个直方图的右边界，但左边界同样要分类讨论。
        while len(stack) > 0:
            prev = stack.pop()
            if len(stack) > 0:
                max_area = max(max_area, (len(heights) - stack[-1] - 1) * heights[prev])
            else:
                max_area = max(max_area, len(heights) * heights[prev])
        return max_area
"""
思路：用一个栈去储存，对于每个元素来说我们只要找到以它为高度的矩形的左边界和右边界的极限在哪里即可。具体方法详见注释。时间复杂度为O(n)，空间复杂度为O(n)。
"""
