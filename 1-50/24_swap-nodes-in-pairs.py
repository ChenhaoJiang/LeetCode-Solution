"""
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.
Ex:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #My code starts here
        re=ListNode(0)
        re.next=head
        #Create a dummy node
        r=re
        while head:
            if not head.next:  #It needs to be swapped when there are at least two nodes left
                break
            
            node=head.next
            head.next=node.next
            node.next=head
            r.next=node
            r=head
            head=head.next
            #Swap every two adjacent nodes
        return re.next
"""
My thinking: Create a dummy node to avoid special case of head node.
"""
