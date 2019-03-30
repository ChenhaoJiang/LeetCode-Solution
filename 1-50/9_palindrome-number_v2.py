
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
        if x < 0 or (x % 10 == 0 and x != 0 ):
            return False
        rev = 0
        while (x > rev) :
            rev = rev *10 + x % 10
            x = x / 10
        return x == rev or x == rev/10
"""
My thinking:将输入的前半部分和后半部分分别存成一个数，然后比较这两个数是否相等。
"""
