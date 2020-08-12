"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
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

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree, your function should populate each next pointer to point to its next right node. 
The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Constraints:
The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000
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
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # 如果根节点为空，则直接返回
        if not root:
            return root
        # 这个node相当于起到一个每层最左节点的作用(leftmost)
        node = root
        # 遍历每一层
        while node.left:
            tmp = node
            # 更新node指针
            node = node.left
            # 在每一层中让tmp指针一直向右移动
            while tmp.next:
                # 左节点的next指针应该指向同个父亲节点下的右节点
                tmp.left.next = tmp.right
                # 右节点的next指针应该指向父亲节点的next节点的左节点
                tmp.right.next = tmp.next.left
                # 更新tmp指针
                tmp = tmp.next
            # 对于每一层的最后一个节点，只需要设置其左节点的next指针，而其右节点的next指针指向None，即为默认值
            tmp.left.next = tmp.right
        return root
"""
思路：使用已建立的next指针，考虑左右节点的两种不同情况，详见注释。算法时间复杂度为O(n)，空间复杂度为O(1)。
"""
