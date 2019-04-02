"""
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
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
input: 3
output: "III"
Ex_2:
input: 4
output: "IV"
Ex_3:
input: 9
output: "IX"
Ex_4:
input: 58
output: "LVIII"
Ex_5:
input: 1994
output: "MCMXCIV"
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        #My code starts here
        dic={1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
        output=""
        for i in dic.keys(): 
        #It's available in Python 3.However, in python, the dictionary cannot be traversed in the initialization order in this way.
            tmp=num//i
            if tmp>0:
                num-=tmp*i
                output+=dic[i]*tmp
        """
        Code in Python:
        dic={1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
        lis=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        output=""
        index=0
        while num>0:
            if num>=lis[index]:
                num-=lis[index]
                output+=dic[lis[index]]
            else:
                index+=1
        """
        return output
"""
My thinking:Use a dictionary to store the corresponding relationship between roman numeral and integer
"""
