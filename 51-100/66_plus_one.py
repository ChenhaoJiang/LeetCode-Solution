"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 从末位开始遍历
        for i in range(len(digits) - 1, -1, -1):
            # 如果该位不是9，则直接该位加1并返回
            if digits[i] != 9:
                digits[i] += 1
                return digits
            # 如果首位是9，则需要在前面添1
            elif i == 0:
                digits[i] = 0
                digits.insert(0,1)
                return digits
            # 如果该位是9，且不是首位，则该位变为0，继续遍历
            else:
                digits[i] = 0
 """
 思路：思路非常简单，只有9是需要特殊考虑的，详见注释。
 """
