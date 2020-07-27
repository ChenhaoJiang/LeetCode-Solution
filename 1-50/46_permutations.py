"""
Given a collection of distinct integers, return all possible permutations.
Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 定义输出为空数组
        output = []
        def backtrack(first = 0):
            for i in range(first, len(nums)):
                # 当所有数字填完时就添加到输出里
                if first == len(nums) - 1:
                    output.append(nums[:])
                else:
                    # 维护一个动态数组
                    nums[i], nums[first] = nums[first], nums[i]
                    # 继续递归填下一个数
                    backtrack(first + 1)
                    # 交换回来即能完成撤销操作
                    nums[i], nums[first] = nums[first], nums[i]
        backtrack(0)
        return output

"""
思路：回溯法的经典例子。时间复杂度为O(n * n!)，其中 n 为序列的长度。除答案数组以外，递归函数在递归过程中需要为每一层递归函数分配栈空间，所以这里需要额外的空间且该空间取决于递归的深度，
空间复杂度为O(n)。
"""
