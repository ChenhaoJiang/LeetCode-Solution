"""
Given a binary tree, return the postorder traversal of its nodes' values.
Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
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
            node = stack.pop()
            # 每次往output中插入值时，都是插在最前面（也就是说最先遍历的节点，其实呈现在结果中在最后）
            output.insert(0, node.val)
            # 如果左节点不为空，则把左节点先压入栈
            if node.left:
                stack.append(node.left)
                
            # 如果右节点不为空，则把右节点压入栈
            # 这样能保证先遍历右子树再遍历左子树
            # 但呈现在结果中，实际上是按照左-右-根的顺序
            if node.right:
                stack.append(node.right)
        return output
"""
思路：递归算法非常容易实现，这题要求用迭代算法。因此设计了一种基于栈的迭代算法，基本的思路就是按照后序遍历的思路（先遍历左子树，随后遍历右子树，最后遍历根节点），因此当一个节点弹出时，我们依次
将其左节点和右节点都压入栈，这样能够证先遍历右子树再遍历左子树。但是我们每次往output中插入值时，都是插在最前面（也就是说最先遍历的节点，其实呈现在结果中在最后），也就是说实际结果是按照左-右-根
的顺序。算法时间复杂度为O(n)，空间复杂度也为O(n)。
"""
