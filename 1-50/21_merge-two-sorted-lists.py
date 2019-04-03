"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two 
lists.
Ex:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #My code starts here
        if not l1:     #If l1 is empty
            return l2
        if not l2:     #If l2 is empty
            return l1
        re=ListNode(0) #Create a dumb node
        r=re
        while l1 or l2:  #Traverse l1 and l2
            if not l1:   #If l1 is traversed
                r.next=l2
                return re.next
            if not l2:   #If l2 is traversed
                r.next=l1
                return re.next
            if l1.val<l2.val:
                r.next=l1
                l1=l1.next
                r=r.next
            else:
                r.next=l2
                l2=l2.next
                r=r.next
  """
  My thinking: Compare the value of the current node of l1 and l2 in turn. 
  """
                
