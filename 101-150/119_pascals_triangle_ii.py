"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
Example:
Input: 3
Output: [1,3,3,1]
Follow up:
Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        # 获取杨辉三角的指定行
        # 由于杨辉三角的每一行其实就是组合数
        # 直接使用组合公式C(n,i) = n!/(i!*(n-i)!)
        # 则第(i+1)项是第i项的倍数=(n-i)/(i+1)
        output = [1] * (rowIndex + 1)
        k = rowIndex
        j = 1
        for i in range(1, rowIndex // 2 + 1):
            output[i] = output[i - 1] * k / j
            k, j = k - 1, j + 1
        # 利用对称性减少一半的计算
        for i in range(rowIndex // 2 + 1, rowIndex + 1):
            output[i] = output[rowIndex - i]
        return output
"""
思路：如果还用动态规划，那么算法时间复杂度过高。本题由于只需要返回杨辉三角的指定行，我们利用杨辉三角的每一行其实就是组合数的特性，并且用组合公式的递推降低时间复杂度，并且利用对称性减少一半的计算。
算法时间复杂度为O(k)，空间复杂度也为O(k)，其中k为行号。
"""
