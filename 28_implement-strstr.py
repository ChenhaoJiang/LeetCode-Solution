"""
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Ex_1:
Input: haystack = "hello", needle = "ll"
Output: 2
Ex_2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #My code starts here
        if not needle:  #If needle is empty, return 0
            return 0
        if len(needle)>len(haystack):  #If the length of needle is larger than the length of haystack, return -1
            return -1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i]==needle[0]:    # When the first character of needle is as same as haystack[i]
                j=0
                while j<len(needle):
                    if haystack[i+j]!=needle[j]:
                        break
                    j+=1
                if j==len(needle):
                    return i
        return -1   #If needle is not part of haystack, return -1
"""
My thinking: Consider the special case and scan each character of haystack.
"""
