"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
Ex_1:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Ex_2:
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #My code starts here
        def isValid(s):   # To define a function to decide if the parentheses substring is valid.
            if not s:
                return True
            li=[]
            for i in range(len(s)):
                if s[i]=='(':
                    li.append(s[i])
                elif not li:
                    return False
                else:
                    li.pop()
            if li:
                return False
            else:
                return True
                
        if not s:
            return 0
        max_len=0
        for i in range(len(s)):
            if s[i]==')':    # The starting parenthesis of a valid parentheses substring can only be open parenthesis.
                continue
            j=1
            length=0
            while i+j<len(s):
                if isValid(s[i:i+j+1]):
                    length=j+1             
                j+=2
            if length>=max_len:
                max_len=length
        return max_len   
"""
My thinking: Time complexity of the algorithm is O(n^3). Generating every possible substring from a string of length n requires O(n^2). 
Checking validity of a string of length n requires O(n). Space complexity of the algorithm is O(1). It's not an efficient algorithm.
"""
  
  
