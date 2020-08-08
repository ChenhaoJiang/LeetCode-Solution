"""
Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. 
If pos is -1, then there is no cycle in the linked list.
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 方法一，将访问过的结点的值改为'visited'
        '''
        # 如果头结点为空，则直接返回False
        if not head:
            return False
        while head.next:
            # 如果遍历到已经访问过的结点则说明有环
            if head.val == 'visited':
                return True
            # 否则将访问过的结点的值改为'visited'
            else:
                head.val = 'visited'
                head = head.next
        return False
        '''
        
        # 方法二，快慢指针法
        if not head:
            return False
        # 设置一个慢指针和一个快指针
        slow = head
        fast = head.next
        # 如果有环存在，那么快指针终究会追上满指针
        while slow != fast:
            # 如果快指针到头了，则返回False
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
"""
思路：本题用了两种方法，第一种方法再不占用额外空间的基础上需要修改原链表，而第二种方法使用了快慢指针法。两种方法时间复杂度均为O(n)，n为链表长度，空间复杂度均为O(1)。
"""
