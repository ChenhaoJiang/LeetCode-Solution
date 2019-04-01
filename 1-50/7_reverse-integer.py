"""
Given a 32-bit signed integer, reverse digits of an integer.
Note:Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
Ex_1:
input:123
output:321
Ex_2:
input:-123
output:-321
Ex_3:
input:95454648484
output:0
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #My code starts here
        num=0
        if x<0:
            sig=0
            x=abs(x)
        #Convert a negative number to a positive number, and then we're going to put a minus sign
        else:
            sig=1 
        while x>0:
            num=num*10+x%10
            x=x//10
        if sig==0:
            num=-num
        if -2**31<num<2**31-1:
            return num
        return 0
"""
My thinking:Pay attention to prevent overflow.
"""
