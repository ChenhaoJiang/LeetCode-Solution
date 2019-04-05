"""
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.
Ex_1:
Input: 1
Output: "1"
Ex_2:
Input: 4
Output: "1211"
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        #My code starts here
        def read(s):   #To define a "read" function
            output=""
            tmp=s[0]
            num=0
            for j in range(len(s)):
                if tmp!=s[j]:   #When it comes to numbers that don't repeat
                    output+=str(num)+str(tmp)
                    tmp=s[j]
                    num=1
                else:
                    num+=1
            output+=str(num)+str(tmp)
            return output
        s="1"
        for i in range(1,n):
            s=read(s)  #Generate the ith term of the count-and-say sequence in turn
        return s
"""
My thinking: The idea is a little bit like looking for duplicates and then generate the ith term of the count-and-say sequence in turn.
"""
