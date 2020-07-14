"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
Example 1:
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:
Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # 返回矩阵的长和宽，如果长或宽为0，则直接返回。
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        if n == 0:
            return
        # 初始化两个布尔变量，用于记录第一行和第一列是否要置0
        rowFlag, columnFlag = False, False
        # 遍历第一列，看第一列是否要置0
        for i in range(m):
            if matrix[i][0] == 0:
                columnFlag = True
                break
        # 遍历第一行，看第一行是否要置0
        for i in range(n):
            if matrix[0][i] == 0:
                rowFlag = True
                break
        # 从矩阵的第二行第二列开始遍历整个矩阵，如果某个元素为0，则用第一行的元素记录哪些列需要置0，以及用第一列的元素来记录哪些行需要置0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # 根据第一行和第一列记录的相关信息，将对应位置的元素置0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        # 根据两个布尔变量来决定是否要将第一行与第一列置0
        if rowFlag:
            for i in range(n):
                matrix[0][i] = 0
     
        if columnFlag:
            for i in range(m):
                matrix[i][0] = 0
  """
  思路：如果说利用一个额外的m*n矩阵来储存这个位置是否要置0，时间上肯定要快很多，但是空间复杂度为O(mn)。当然也可以用一个m维向量和n维向量分别储存每一行和每一列是否要置0，这样空间复杂度为
  O(m+n)。由于题目要求是希望以空间为主，空间复杂度希望为O(1)，并且要在原矩阵上直接修改，因此本题只能用这种方法来做。
  """
