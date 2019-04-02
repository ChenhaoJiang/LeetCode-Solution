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
        if len(strs)>=2:
            min_len=min(len(strs[i]) for i in range(len(strs)))
        elif len(strs)==1:
            return strs[0]
        else:
            return ""
        output=""
        for i in range(min_len):
            s=strs[0][i]
            for j in range(len(strs)):
                if strs[j][i]!=s:
                    return output
            output+=s
        return output   
  """
  My thinking: Compare each character in turn for each string
  """
