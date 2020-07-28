"""
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]
Output: true
Example 2:
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]
Output: false
Example 3:
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]
Output: false
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # 终止条件，两个结点都为空，则相等
        if not p and not q:
            return True
        # 如果两个结点一个为空，那肯定两棵树不相等
        # 或者两个结点的值不相等，那肯定两棵树也不相等
        elif not p or not q or p.val != q.val:
            return False
        # 否则则递归返回两棵树的左右结点是否对应相等
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
 """
 思路：递归法，时间复杂度为：O(N)，其中 N 是树的结点数，因为每个结点都访问一次。空间复杂度: 最优情况（完全平衡二叉树）时为O(log(N))，最坏情况下（完全不平衡二叉树）时为O(N)，用于维护递归栈。
 """
