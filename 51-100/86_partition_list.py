"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # 定义两个哑结点来储存前后两条链，可以减少条件的判断
        # 同时定义两个结点随着前后两条链动
        before_head = before = ListNode(0)
        after_head = after = ListNode(0)
        # 对原来的链的每个结点进行判断，是应该接在前面那条链还是后面
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        # 防止出现闭环而导致时间溢出
        after.next = None
        # 将前后两条链接起来
        before.next = after_head.next
        # 返回结果
        return before_head.next

"""
思路：设置两条链来分别储存前面的结点和后面的结点。定义两个哑结点来储存前后两条链，可以减少条件的判断。最后要把闭环断开，否则会导致时间溢出。时间复杂度为O(n)，空间复杂度为O(1)。
"""
