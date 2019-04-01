"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
Ex_1:
Input: "()"
Output: true
Ex_2:
Input: "()[]{}"
Output: true
Ex_3:
Input: "(]"
Output: false
Ex_4:
Input: "([)]"
Output: false
Ex_5:
Input: "{[]}"
Output: true
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #My code starts here
        string=[]   #To initial a stack
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                string.append(s[i])   #Push the open brackets onto the stack
            if s[i]==')':
                if len(string)==0 or string.pop()!='(':
                    return False
            if s[i]==']':
                if len(string)==0 or string.pop()!='[':
                    return False
            if s[i]=='}':
                if len(string)==0 or string.pop()!='{':
                    return False 
    
        if len(string)==0:
            return True
        else:
            return False
"""
My thinking: Use a stack to store open brackets.When we encounter a closing bracket, then check the element on top of the stack. If the element at the top of the stack is an opening bracket of the same type, then pop it off the stack. Else, this implies an invalid expression. In the end, if we are left with a stack still having elements, then this implies an invalid expression.
"""
