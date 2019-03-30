"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
Ex_1:
input:121
output:true
Ex_2:
input:10
output:false
Ex_3:
input:-121
output:false
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #My code strats here
        num=[]
        if x<0:
            return False
        while x>0:
            num.insert(0,x%10)
            x=x//10
        #To store each digit of input in a list

        length=len(num)
        for index in range(length//2):
            if num[index]!=num[length-index-1]:
                return False
        return True
"""
My thinking:如果输入为负，则不是回文数。然后，将输入的每一位都存在list里，然后将list的第一个元素和最后一个元素比较，第二个元素和倒数第二个元素比较，以此类推，如果每次比较都相等，则这个数为回文数。否则，则不是回文数。中间那一位不需要比较，因此只需要比较length//2次。
"""

