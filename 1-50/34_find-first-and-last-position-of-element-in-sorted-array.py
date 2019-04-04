"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
Ex_1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Ex_2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #My code starts here
        low=0
        high=len(nums)
        while low<high:
            middle=(low+high)//2
            if target<=nums[middle]:
                high=middle
            else:                
                low=middle+1
        #Find the starting position
        
        if low==len(nums) or nums[low]!=target:
            return [-1,-1]
        #Target is not in the list.
        
        index_left=low
        low=0
        high=len(nums)
        while low<high:
            middle=(low+high)//2
            if target<nums[middle]:
                high=middle
            else:                
                low=middle+1
        #Find the ending position
        index_right=low-1
        return [index_left,index_right]
"""
My thinking: Use binary search. The starting and ending positions are found in slightly different ways.
"""
