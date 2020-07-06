"""
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.
Example 1:
Input: a = "11", b = "1"
Output: "100"
Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
Constraints:
Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # length为最长长度
        length = max(len(a), len(b))
        # 储存进位
        carry = 0
        # 初始化输出字符串
        c = ''
        # 遍历
        for i in range(- 1, -length - 1, -1):
            m = int(a[i]) if i > -len(a) - 1 else 0
            n = int(b[i]) if i > -len(b) - 1 else 0 
            c = str((m + n + carry)%2) + c
            carry = int((m + n + carry)/2)
        # 如果仍有进位，则加一位
        if carry == 1:
            c = '1' + c
        return c
        """
        # 充分利用python内置函数，int(string,base=2)将string（二进制表示）转化为整数，bin()函数将整数用二进制表示（前两位为0b)
        return bin(int(a,2)+int(b,2))[2:]
        """
"""
思路：第一种方法直接就是利用了二进制的计算，考虑进位即可。第二种方法利用了python的内置函数，int(string,base=2)将string（二进制表示）转化为整数，bin()函数将整数用二进制表示（前两位为0b)。
"""
