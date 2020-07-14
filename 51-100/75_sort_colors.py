"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, 
white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.
Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 设置三个变量，left记录左边界即有多少个0，right记录右边界即有多少个2，index为当前遍历对象的索引
        index, left, right = 0, 0, len(nums) - 1
        while index <= right:
            # 如果当前对象为0，则把它与左边界位置对应的元素交换
            if nums[index] == 0:
                nums[index], nums[left] = nums[left], nums[index]
                left += 1
                index += 1
            # 如果当前对象为2，则把它与右边界位置对应的元素交换
            # 但是此时index不能够加1，因为交换过来的元素不排除有为0的可能性
            elif nums[index] == 2:
                nums[index], nums[right] = nums[right], nums[index]
                right -= 1
            else:
                index += 1
 """
 思路：本问题被称为荷兰国旗问题，由于只能遍历一次数组，所以只能采用这样的方法。即：碰到0就把0放在最前面，碰到2就把2放在最后面，中间全是1，自然就排好了。
