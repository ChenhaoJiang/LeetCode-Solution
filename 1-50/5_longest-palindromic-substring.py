"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Ex_1:
input:"babad"
output: "bab"
Note: "aba" is also a valid answer.
Ex_2:
input: "cbbd"
output: "bb"
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #My code starts here
        max_len=0  #Define the length of a longest palindromic substring
        output=""  #Default output is ""
        for i in range(len(s)):
            tmp_output=s[i]
            tmp_len=1
            min_index=i
            max_index=i
            while max_index+1<len(s) and s[max_index+1]==s[min_index]:
                tmp_len+=1
                max_index+=1
                tmp_output+=s[max_index]
            #Find the longest identical string

            while min_index>0 and max_index<len(s)-1 and s[min_index-1]==s[max_index+1]:
                tmp_len+=2
                tmp_output=s[min_index-1]+tmp_output+s[max_index+1]
                min_index-=1
                max_index+=1
            #Compare whether the characters on both sides are equal

            if tmp_len>max_len:
                output=tmp_output
                max_len=tmp_len
            
        return output
"""
My thinking: First step, find the longest identical string. Then, on the basis of the first step, compare whether the characters on both
sides are equal. At last, compare the length of the longest palindromic substring found by the current loop to the global variable 
'max_len'.
"""
