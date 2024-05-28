'''
143. Reorder List

Difficulty: Medium
Topics: Linked List, Two Pointers, Stack, Recursion

You are given the head of a singly-linked list.
The list can be represented as:

    L0 -> L1 -> ... Ln-1 -> Ln

Reorder the list to be on the following form:

    L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...

You may not modify the values in the list's nodes.
Only nodes themselves may be changed.

I remember this was a daily from March.
My friend, Adrian (AdrianG0954), recommended me to do it
during our Algoritms course.
I don't think I'll make a folder specifically for the dailies
in March since that was a long time ago and I wasn't fully
committed on doing Leetcode at the time. I was more focused
on passing the Algoritms course more than anything
O(n) time, O(n) space submission

This was also when I realized the "->" after a function def 
probably means the return type. 
This function does not have one.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        rep = []
        curr = head
        length = 0
        while curr:
            rep.append(curr)
            length += 1
            curr = curr.next
        
        start = 0
        end = length - 1
        while start < end:
            rep[start].next = rep[end]
            start += 1
            rep[end].next = rep[start]
            end -= 1
        rep[start].next = None



