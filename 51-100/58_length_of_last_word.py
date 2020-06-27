"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word 
if we loop from left to right) in the string.
If the last word does not exist, return 0.
Note: A word is defined as a maximal substring consisting of non-space characters only.
Example:
Input: "Hello World"
Output: 5
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Solution 1
        """
        num = 0
        prev = 0
        flag = False # 这个标志用来记录最后是不是以空格结尾
        for i in range(len(s)):
            # 遇到空格，则将单词长度置为0
            if s[i] == ' ' and flag == True:
                prev = num
                num = 0
                flag = False
            elif s[i] != ' ':
                flag = True
                num += 1
        return num if flag else prev   # 如果最后是以空格结尾，则返回之前那个单词的长度
        """
        # Solution 2
        s = s.split()
        return len(s[-1]) if s else 0
"""
思路：第一种解法是顺序遍历字符串的方法，唯一需要特殊处理的地方就是可能会存在最后以空格为结尾的情况，因此引入一个flag进行判断。第二种解法直接用了python内置的split()函数，对字符串进行按空格分
割，并返回最后一个词的长度即可。评论里也看到一种做法，用strip()函数去除字符串末尾的空格，再用普通做法做。既然都用了strip()了，为什么不直接split()呢？
"""
