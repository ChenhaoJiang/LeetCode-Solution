"""
Given a binary tree, return the inorder traversal of its nodes' values.
Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 基于栈的迭代算法
        # 定义一个栈
        stack = []
        output = []
        while True:
            # 迭代把当前的root节点的所有的左节点都压入栈
            while root:
                stack.append(root)
                root = root.left
            # 用while True + if break的结构，实现了类似于do while的功能
            if not stack:
                break
            # 依次把栈中节点弹出
            node = stack.pop()
            output.append(node.val)
            # 如果该节点有右结点，则将右节点设为root（也就是在下一次迭代的时候，会将右节点的所有左节点都压入栈）
            if node.right:
                root = node.right
        return output
 """
 思路：递归算法非常容易实现，这题要求用迭代算法。因此设计了一种基于栈的迭代算法，基本的思路就是按照中序遍历的思路（先遍历左子树，随后遍历根节点，最后遍历右子树），因此我们先将一个节点的所有左
 节点都压入栈，然后依次弹出，如果弹出的节点有右节点，那么我们再将右节点的所有左节点都压入栈。算法时间复杂度为O(n)，空间复杂度也为O(n)。
 """
