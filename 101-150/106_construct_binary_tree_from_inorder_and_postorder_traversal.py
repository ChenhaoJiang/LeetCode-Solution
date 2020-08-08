"""
Given inorder and postorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.
For example, given
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # 递归算法
        # 如果中序遍历的数组为空，则返回根节点为空
        if not inorder:
            return None
        # 后序遍历数组的最后一个元素为树的根节点
        root = TreeNode(postorder[-1])
        # 在中序遍历的数组中找到根节点对应元素的下标
        index = inorder.index(postorder[-1])
        # 那么我们就可以知道左子树节点数以及右子树节点数，并且中序遍历数组中这个下标前的元素对应的左子树部分，这个下标后的元素对应的右子树部分。
        # 采用递归算法进行构建即可。
        root.left = self.buildTree(inorder[0:index], postorder[0:index])
        root.right = self.buildTree(inorder[index + 1:], postorder[index:-1])
        return root
"""
思路：因为二叉树后序遍历的顺序为：先递归地遍历左子树，随后递归地遍历右子树，最后遍历根节点。二叉树中序遍历的顺序为：先递归地遍历左子树，随后遍历根节点，最后递归地遍历右子树。因此，对于任意一颗树而
言，后序遍历的形式总是[[左子树的前序遍历结果], [右子树的前序遍历结果], 根节点]，即根节点总是后序遍历中的最后一个节点。而中序遍历的形式总是[[左子树的中序遍历结果], 根节点, [右子树的中序遍历结果]]。
因此本题采用递归算法，详见注释。时间复杂度为O(n)，其中n是树中的节点个数。空间复杂度为O(h)，因为我们需要O(h)（其中 h 是树的高度）的空间表示递归时栈空间。
"""
