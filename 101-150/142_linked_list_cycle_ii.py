"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. 
If pos is -1, then there is no cycle in the linked list.
Note: Do not modify the linked list.
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
Follow-up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 定义一个慢指针和一个快指针
        slow, fast = head, head
        while True:
            # 如果快指针到头了，则说明链表中没有环
            if not fast or not fast.next:
                return None
            # 慢指针每次前进一步
            slow = slow.next
            # 快指针每次前进两步
            fast = fast.next.next
            # 如果快指针赶上了慢指针，那就说明链表中有环，而且fast - slow = nb（b为环的长度)
            # 而fast = 2 * slow ,因此此时slow走了nb步，其中n未定，但为一个正整数。
            if slow == fast:
                break
        # 让fast从head开始
        fast = head
        # 当fast和slow再次相遇时，fast应该走了a步到达环的开始，slow走了a+nb步也到了环的开始，此时两个指针所在的结点就是所求。
        # 其中a为从头结点到环的开始的长度。
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast
"""
思路：快慢指针法，当快慢指针第一次相遇时，那就说明链表中有环，而且fast - slow = nb（b为环的长度)。而fast = 2 * slow ,因此此时slow走了nb步，其中n未定，但为一个正整数。让fast从head开始，
并且fast也改为每次走一步，这样当fast和slow再次相遇时，fast应该走了a步到达环的开始，slow走了a+nb步也到了环的开始，此时两个指针所在的结点就是所求(其中a为从头结点到环的开始的长度)。算法时间
复杂度为O(n)，因为第二次相遇中，慢指针须走步数 a<a+b；第一次相遇中，慢指针须走步数 a+b−x<a+b，其中x为双指针重合点与环入口距离；因此总体为线性复杂度。空间复杂度为O(1)，因为双指针使用常数大
小的额外空间。
"""
