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
        if not s or len(s)==1:
            return 0
        store=[0 for i in range(len(s))]
        for i in range(len(s)):
            if s[i]=='(':     # The ending parenthesis of a valid parentheses substring can only be closing parenthesis.
                continue
            if i-1>=0 and s[i-1]=='(':
                if i-2>=0:
                    store[i]=store[i-2]+2
                else:
                    store[i]=2
            if (i-1>=0 and s[i-1]==')') and (i-store[i-1]-1>=0 and s[i-store[i-1]-1]=='('):
                if i-store[i-1]-2>=0: 
                    store[i]=store[i-1]+store[i-store[i-1]-2]+2
                else:
                    store[i]=store[i-1]+2
        return max(store)
"""
My thinking: We make use of a "store" array where ith element of "store" represents the length of the longest valid substring ending at ith 
index. Using dynamic programming. It's obvious that the valid substrings must end with '('. Time complexity of the algorithm is O(n), 
because single traversal of string to fill "store" array is done. Space complexity of the algorithm is O(n), because "store" array of size 
n is used. 
"""
