"""
Given a sorted linked list, delete all duplicates such that each element appear only once.
Example 1:
Input: 1->1->2
Output: 1->2
Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 如果头结点为空，则直接返回
        if not head:
            return head
        # 储存头结点
        node = head
        # 一直遍历到链表的末端
        while node.next:
            # 如果当前结点的值与下个结点的值相等，则删除掉下个结点
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
 """
 思路：本题思路比较简单且明确，即遍历整个链表，如果碰到相同的值，则进行删除。时间复杂度为O(n)，空间复杂度为O(1)。
 """
