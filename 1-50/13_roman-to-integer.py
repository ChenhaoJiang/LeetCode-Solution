"""
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
Note:There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Ex_1:
input:"III"
output:3
Ex_2:
input: "IV"
output: 4
Ex_3:
input: "IX"
output: 9
Ex_4:
input: "LVIII"
output: 58
Ex_5:
input: "MCMXCIV"
output: 1994
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #My code starts here
        num=0
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)):
            num=num+dict[s[i]]
            if i>0:
                if (s[i]=='M' or s[i]=='D') and s[i-1]=='C':
                    num=num-200
                if (s[i]=='L' or s[i]=='C') and s[i-1]=='X':
                    num=num-20
                if (s[i]=='V' or s[i]=='X') and s[i-1]=='I':
                    num=num-2
        return num
"""
My thinking: Use a dictionary to store correspondence, and pay attention to special cases
"""
