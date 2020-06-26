"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划
        sums = 0 
        max_sum = nums[0] #储存当前的最大和
        for i in range(len(nums)):
            max_sum = max(sums+nums[i], max_sum)  # 倘若子数组和大于当前最大和，则替换
            sums = max(sums + nums[i], 0)         # 倘若子数组和小于0，则舍去
        return max_sum   
        
"""
思路：采用动态规划，当子数组和小于0时，这部分和对于最大和来说不应该有贡献，因此需舍去。（分治法还没搞懂...)
"""
