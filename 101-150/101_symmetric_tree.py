"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 如果这棵树为空，则直接返回True
        if not root:
            return True
        # 定义一个递归函数
        def dfs(left, right):
            # 递归的终止条件是两个结点都为空
            if not left and not right:
                return True
            # 或者两个结点中有一个为空
	    # 或者两个结点的值不相等
            elif not left or not right or left.val != right.val:
                return False
            # 否则则将左半边树的左结点与右半边树的右结点进行比较，将左半边树的右结点与右半边树的左结点进行比较
            else:
                return dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right)
"""
思路：递归算法。算法的时间复杂度是O(n)，因为要遍历n个节点空间复杂度是O(n)。空间复杂度是递归的深度，也就是跟树高度有关，最坏情况下树变成一个链表结构，高度是n。
"""
