"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Ex_1:
Input: ["flower","flow","flight"]
Output: "fl"
Ex_2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:
All given inputs are in lowercase letters a-z.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #My code starts here
        if not strs:
            return ""
        output = ""
        for chars in zip(*strs):
            if len(set(chars)) ==1:
                output += chars[0]
            else:
                break
        return output
"""
My thinking: Use zip() function to access strings parallelly.
"""
