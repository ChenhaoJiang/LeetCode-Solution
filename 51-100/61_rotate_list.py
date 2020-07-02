"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.
Example 1:
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 特殊情况
        if not head:
            return None
        if not head.next:
            return head
        old_tail = head
        # 用来统计链表的长度
        length = 1
        # 找到原先的尾部
        while old_tail.next:
            old_tail = old_tail.next
            length += 1
        # 先把链表闭成环
        old_tail.next = head
        # 找到新的尾部 : (length - k % length - 1)th node
        # 和新的头部 : (length - k % length)th node
        new_tail = head
        for i in range(length - k % length - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        # 断开闭环
        new_tail.next = None
        return new_head
"""
思路：先找到原先的尾结点，将链表闭成环。再根据length - k % length - 1找到新的尾结点以及length - k % length找到新的头结点，从此处断开即可。
"""
