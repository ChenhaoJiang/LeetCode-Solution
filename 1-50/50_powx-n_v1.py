"""
mplement pow(x, n), which calculates x raised to the power n (x^n).
Ex_1:
Input: 2.00000, 10
Output: 1024.00000
Ex_2:
Input: 2.10000, 3
Output: 9.26100
Ex_3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
Note:
-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        #My code starts here
        res = self.pow(x, abs(n))
        if n < 0:
            res = 1.0 / res  #When n<0, pow(x,n)=1/pow(x,abs(n)).
        return res
    
    def pow(self, x, n):
        if n == 0: 
            return 1
        res = self.pow(x, n // 2)  #Binary recursive
        res *= res
        if n % 2:
            res *= x
        return res
"""
My thinking: When n<0, pow(x,n)=1/pow(x,abs(n)). So we only need to consider the situation where n>=0. Then we implement this function 
recursively.
"""
