'''
206. Reverse Linked List

Difficulty: Easy
Topics: Linked List, Recursion

Given the head of a singly linked list, reverse the List
and return the reversed list.

Nun' much to say. Just pointer switching
O(n)
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        return prev
