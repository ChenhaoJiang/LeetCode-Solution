"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        m , n = len(matrix) , len(matrix[0])  # 返回矩阵的长和宽
        visited = [[False] * n for _ in range(m)]  # 生成一个矩阵记录是否已遍历
        output = []
        x , y = 0 , 0  # 定义当前点的坐标
        direction = 0  # 定义移动的方向
        len_path = 0    # 用来判断什么时候结束循环(路径的长度)
        move_map = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 定义对应的移动
        while len_path != m*n:
            len_path += 1
            output.append(matrix[x][y])
            visited[x][y] = True
            next_x , next_y = x + move_map[direction][0] , y + move_map[direction][1]
            # 判断一下下一个点是不是已经遍历过了或者是不是超出范围，如果是则改变方向
            if next_x == m or next_x == -1 or next_y == n or next_y == -1 or visited[next_x][next_y] == True:
                direction = (direction + 1) % 4
            x , y = x + move_map[direction][0] , y + move_map[direction][1]
        return output
"""
思路：用一个矩阵来记录已经遍历过的点，然后让一个点依次以右下左上四个顺序来遍历螺旋矩阵。当碰到已经遍历过了或者超出范围的点，则变换方向。这种做法时间复杂度为O(mn)，但空间复杂度较高，也为O(mn)。
"""
