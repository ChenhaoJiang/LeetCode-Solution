"""
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.
Example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 如果这颗树的根节点为空，则说明这颗树的深度为0。
        if not root:
            return 0
        # 左子树的深度
        left_depth = self.maxDepth(root.left)
        # 右子树的深度
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1
        
"""
思路：假设我们知道了左子树和右子树的最大深度 l 和 r，那么该二叉树的最大深度即为max(l,r)+1。因此使用递归算法即可。时间复杂度：O(n)，其中n为二叉树节点的个数。每个节点在递归中只被遍历一次。
空间复杂度：O(h)，其中h表示二叉树的高度。递归函数需要栈空间，而栈空间取决于递归的深度，因此空间复杂度等价于二叉树的高度。
"""
