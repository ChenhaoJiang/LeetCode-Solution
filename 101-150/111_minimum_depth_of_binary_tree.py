"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.
Example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 递归算法
        # 如果根节点为空，那么最小深度直接为0
        if not root:
            return 0
        # 如果根节点既没有左节点也没有右节点，那么最小深度直接为1
        if not root.left and not root.right:
            return 1
        # 如果根节点没有左节点但是有右节点，那么左子树就没有叶子节点了，最小深度完全取决于右子树（即右子树的最小深度 + 1）
        elif not root.left:
            return self.minDepth(root.right) + 1
        # 如果根节点没有右节点但是有左节点，那么右子树就没有叶子节点了，最小深度完全取决于左子树（即左子树的最小深度 + 1）
        elif not root.right:
            return self.minDepth(root.left) + 1
        # 如果根节点既有左节点也有右节点，那么最小深度就应该是左子树的最小深度和右子树的最小深度中较小的那个 + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
"""
思路：本题采用递归算法，算法思路详见注释。算法时间复杂度为O(n)，其中n为节点个数，因为我们访问每个节点一次。算法空间复杂度完全取决于数的高度，即为O(h)。在最坏情况下，整棵树是非平衡的，例如每个
节点都只有一个孩子，递归会调用 n（树的高度）次，因此栈的空间开销是O(n)。但在最好情况下，树是完全平衡的，高度只有log(n)，因此在这种情况下空间复杂度只有O(log(n)) 。
"""
