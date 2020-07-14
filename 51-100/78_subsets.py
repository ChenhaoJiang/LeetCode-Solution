"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ### 解法一 ###
        # 返回nums的长度
        n = len(nums)
        # 定义一个空的list记录输出
        output = []
        # 生成0.00到1.11的字符串，每个字符串记录哪些元素需要被加到list里
        # 这里很妙的一个地方在于是将2^n到2^(n+1)-1转化为二进制，并少取前面一位；否则转化为二进制可能会丢失掉前面的0，会很麻烦。
        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            
            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
        return output
        
        ### 解法二 ###
        # 利用递归的思想
        """
        # 返回nums的长度
        n = len(nums)
        # 定义一个list记录输出，这里初始里面就含有一个元素为[]
        output = [[]]
        # 每增加一个元素，做法为先复制原有输出，一份保持不动，另一份均添加新来的元素。
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output
        """
        
"""
思路：两种做法详见注释，一种为依靠二进制排序的做法，另一种为递归法。两种做法的时间复杂度均为O(n*2^n)，空间复杂度也均为O(n*2^n)。
"""
