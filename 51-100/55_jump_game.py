"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        max_length = 0  # 初始化当前能到达的最远位置
        for i , num in enumerate(nums):  # 遍历整个数组
            # 如果当前位置能到达，并且从当前位置出发能超过最远位置，则更新最远位置
            if max_length >= i and i + num > max_length: 
                max_length = i + num
        # 比较最远位置和数组最后一个元素的位置
        return max_length >= len(nums) - 1 
        
"""
思路：贪心算法，尽可能到达最远位置。如果能到达某个位置，那一定能到达它前面所有位置。对能够到达的位置，比较从当前位置出发是否能超过最远位置，如果能，则更新最远位置。时间复杂度O(n)，空间复杂度O(1)。
"""
