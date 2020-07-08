"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 本质上就是一个斐波那契数列，climbStairs(n) = climbStairs(n - 1) + climbStairs(n - 2)
        cur = 1
        pre = 0
        i = 0
        # 使用动态规划即可
        while i < n:
            num = cur
            cur += pre
            pre = num
            i += 1
        return cur 
"""
思路：使用动态规划实现一个斐波那契数列，时间复杂度为O(n)。同样也可以直接利用斐波那契数列的通项公式来完成这题，时间复杂度为O(logn)。
"""
