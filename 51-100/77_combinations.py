"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
Example:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        candidates = [i for i in range(1,n + 1)]
        # index_list 起始为[0,1,...,k-1]，主要记录当前一次遍历要取candidates里的哪些元素
        index_list = [i for i in range(k)]
        # 定义一个空的list存放输出
        output = []
        index = -1
        # 循环结束条件为index_list变为[n-k,...,n-2,n-1]，即sum(index_list) = (2 * n - k - 1) * k / 2
        while sum(index_list) != (2 * n - k - 1) * k / 2:
            # 每一次都按照index_list，把candidates里要取的元素组成一个新的list添加到output里
            output.append([candidates[i] for i in index_list])
            # 每一次都先让index_list的最后一位开始加，直到加到n-1为止，然后将前一位加1，最后一位调整为前一位加1，再让最后一位开始加，直到加到n-1为止。
            # 而每一位最多不能超过n+i，i表示倒数第i位
            output.append([candidates[i] for i in index_list])
            if index_list[index] == n + index:
                # 从最后一位开始找，直到找到还没到n+i的那一位，i表示倒数第i位
                while index_list[index] == n + index:
                    index -= 1
                # 给那一位加1
                index_list[index] += 1
                # 然后把后面的每一位置位前一位加1
                for i in range(index + 1, 0, 1):
                    index_list[i] = index_list[i - 1] + 1
                index = -1
            else:
                index_list[index] += 1
        output.append([candidates[i] for i in index_list])
        return output
 """
 思路：本题思路比较绕，详见注释。
 """
