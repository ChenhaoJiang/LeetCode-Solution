"""
Given a binary tree
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
Follow up:
You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
Example 1:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree , your function should populate each next pointer to point to its next right node. 
The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Constraints:
The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def processChild(self, childNode, prev, leftmost):
        # 如果当前孩子节点为空，那就可以直接跳过这个节点了
        if childNode:
            # 如果当前孩子节点和prev都不为空，则将prev的next指针指向当前孩子节点
            if prev:
                prev.next = childNode
            else:
                # 如果当前孩子节点不为空，而prev为空，说明这个孩子节点是这层的最左节点
                leftmost = childNode
            # 把prev赋给这个孩子节点
            prev = childNode
        return leftmost, prev
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # 如果根节点为空，则直接返回
        if not root:
            return root
        # leftmost节点指向每一层的最左边
        leftmost = root
        # 遍历每一层
        while leftmost:
            # cur节点指向当前节点，prev节点指向上一个孩子节点
            cur, prev = leftmost, None
            # 重新设置leftmost，这里是为了断开最外层的环
            leftmost = None
            # cur节点遍历当前层的每一个节点，processChild为当前层每一个节点的孩子节点生成next指针
            while cur:
                # 为当前层每一个节点的左孩子和右孩子分别生成next指针
                leftmost, prev = self.processChild(cur.left, prev, leftmost)
                leftmost, prev = self.processChild(cur.right, prev, leftmost)
                # 更新cur指针
                cur = cur.next
        return root
"""
思路：我们依旧使用已建立的next指针，详见注释。这道题和116题区别在于，116题给的是完美二叉树，因此我们只需考虑左右节点的不同，因为除了每一层的最右节点，我们一定都能找到其next指针对应的节点，但是
这道题不一样，相邻的右节点可能为空，我们需要用一个prev指针记录上一个孩子节点，当碰到新的不为空的孩子节点时，就将prev的next指针指向这个新的孩子节点。算法时间复杂度为O(n)，空间复杂度为O(1)。
"""
