"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were 
inserted in order.
You may assume no duplicates in the array.
Ex_1:
Input: [1,3,5,6], 5
Output: 2
Ex_2:
Input: [1,3,5,6], 2
Output: 1
Ex_3:
Input: [1,3,5,6], 7
Output: 4
Ex_4:
Input: [1,3,5,6], 0
Output: 0
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #My code starts here
        if not nums:
            return 0
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        return len(nums)
"""
My thinking: Use sequential search.
"""
