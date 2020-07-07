"""
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
Example 1:
Input: 4
Output: 2
Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 二分法
        # 左边界初始化为0，主要考虑到x可能为0
        left = 0
        # 右边界初始化为x//2+1，主要考虑到x可能为1
        right = x // 2 + 1
        # 迭代
        while left < right:
            mid = (left + right + 1) // 2
            square = mid * mid
            if square > x:
                right = mid - 1
            elif square < x:
                left = mid
            else:
                return mid
        return left
        """
        # 牛顿法（用一阶泰勒展式（即在当前点的切线）代替原曲线）
        cur = 1
        # 当误差在精度允许范围内，则停止迭代
        while abs(cur - pre) > 1e-6:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(round(cur))
        """
"""
思路：二分法的思路比较简单，时间复杂度为O(logN)，空间复杂度为O(1)。牛顿法使用一阶泰勒展式（即在当前点的切线）代替原曲线，需要进行一定数学演算。但很奇怪这题总是超出时间限制。
"""
