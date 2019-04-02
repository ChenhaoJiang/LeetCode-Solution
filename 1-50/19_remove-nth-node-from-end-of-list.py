"""
Given a linked list, remove the n-th node from the end of list and return its head.
Ex:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #My code starts here
        re=head
        node=re
        #Use two pointers to traverse the list
        for i in range(n):
            if node.next==None:  #Consider the case where the node you want to delete is head node
                re=re.next
                return re
            node=node.next
        while node.next:
            node=node.next
            head=head.next
        head.next=head.next.next
        return re
"""
My thinking: Use two pointers. Both pointers are exactly separated by n nodes apart. We maintain this constant gap by advancing both 
pointers together until the first pointer arrives past the last node. The second pointer will be pointing at the nth node counting from the
last. We relink the next pointer of the node referenced by the second pointer to point to the node's next next node.
"""
