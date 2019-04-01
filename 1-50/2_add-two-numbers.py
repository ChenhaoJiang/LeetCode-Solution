"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Ex:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #My code starts here
        re = ListNode(0)
        r=re
        carry=0   #Consider carry
        while l1 or l2:  
            x= l1.val if l1 else 0
            y= l2.val if l2 else 0
            #Consider the numbers of the digits of l1,l2 are different
            s=carry+x+y
            carry=s//10   
            r.next=ListNode(s%10)
            r=r.next 
            if l1:l1=l1.next
            if l2:l2=l2.next 
        if carry>0:
            r.next=ListNode(1)
        return re.next
"""
My thinking: Keep track of the carry using a variable and simulate digits-by-digits sum starting from the head of list, which contains the least-significant digit.
"""

