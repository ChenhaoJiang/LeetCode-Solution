"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
Note: A leaf is a node with no children.
Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # 如果是空节点，则直接返回False
        if not root:
            return False
        # 如果该节点是叶子节点，则判断val和sum是不是相等
        if not root.left and not root.right:
            return root.val == sum
        # 递归判断左右节点
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
"""
思路：递归法，详见注释。算法时间复杂度：O(n)，其中n是树的节点数，因为对每个节点都只访问一次。空间复杂度：O(h)，其中h是树的高度。空间复杂度主要取决于递归时栈空间的开销，最坏情况下，树呈现链状，
空间复杂度为O(n)。平均情况下树的高度与节点数的对数正相关，空间复杂度为O(log n)。
"""
