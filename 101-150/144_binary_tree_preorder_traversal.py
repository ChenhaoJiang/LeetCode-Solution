"""
Given a binary tree, return the preorder traversal of its nodes' values.
Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 基于栈的迭代算法
        # 定义一个栈
        stack = []
        output = []
        # 先将根节点压入栈
        if root:
            stack.append(root)
        while stack:
            # 依次弹出栈中元素
            node = stack.pop()
            output.append(node.val)
            # 如果右节点不为空，则把右节点先压入栈
            if node.right:
                stack.append(node.right)
            # 如果左节点不为空，则把左节点压入栈
            # 这样能保证先遍历左子树再遍历右子树
            if node.left:
                stack.append(node.left)
        return output
 """
 思路：递归算法非常容易实现，这题要求用迭代算法。因此设计了一种基于栈的迭代算法，基本的思路就是按照前序遍历的思路（先遍历根节点，随后遍历左子树，最后遍历右子树），因此当一个节点弹出时，我们依次
 将其右节点和左节点都压入栈，这样能够证先遍历左子树再遍历右子树。算法时间复杂度为O(n)，空间复杂度也为O(n)。
 """
