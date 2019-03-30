"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
Ex:
input: nums = [2, 7, 11, 15], target = 9
output: [0,1]
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #My code starts here

        map={}
        for index,num in enumerate(nums):
            another_num=target-num
            if another_num in map:
                return [map[another_num],index]
            map[num]=index
        return None
"""
My thinking:采用字典的做法，将nums数组中的数和对应的下标存入字典中
"""
