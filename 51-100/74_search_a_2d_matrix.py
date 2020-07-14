'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ### 解法一 ###
        # 记录矩阵的长和宽，如果为0，则直接返回False
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        # 先对每一行的开头做一个二分查找，如果搜索到了直接返回True，没有搜索到的话则确定只可能在哪一行
        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[mid][0]:
                return True
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
        # index记录只能在哪一行
        index = right
        # 对可能的那一行做二分查找
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[index][mid]:
                return True
            elif target < matrix[index][mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False
        
        '''
        ### 解法二 ###
        # 直接对m*n个元素二分查找
        left, right = 0, m * n - 1
        while left <= right:
                mid= (left + right) // 2
                # 将索引转化为对应的元素
                mid_element = matrix[mid // n][mid % n]
                if target == mid_element:
                    return True
                else:
                    if target < mid_element:
                        right = mid_idx - 1
                    else:
                        left = mid_idx + 1
        return False
        '''
  '''
  思路：两种解法总体上来说都是利用二分查找，因此时间复杂度均为O(log(mn))，空间复杂度均为O(1)。
  '''
