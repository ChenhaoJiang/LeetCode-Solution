"""
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.
In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level.
Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory 
name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.
Example 1:
Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:
Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:
Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
Example 4:
Input: "/a/./b/../../c/"
Output: "/c"
Example 5:
Input: "/a/../../b/../c//.//"
Output: "/c"
Example 6:
Input: "/a//b////c/d//././/.."
Output: "/a/b/c"
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # 定义一个栈去储存路径
        candidates = []
        # 将路径按'/'分隔并遍历
        for candidate in path.split('/'):
            # 如果不是'//'、'/./'、'/../'这三种特殊情况，则正常处理，否则前两种删除
            if candidate not in ['', '.', '..']:
                candidates.append(candidate)
            # 如果是'/../'这种情况，则要判断前面还有没有别的路径，如果有，则需要删除上一层
            elif candidate == '..' and candidates:
                candidates.pop()
        # 最后用'/'连接并输出
        return '/' + '/'.join(candidates)
"""
思路：考虑三种特殊情况'//'、'/./'、'/../'，用一个栈去储存两个'/'之间的元素，最后用'/'连接并输出。
"""
