'''
234. Palindrome Linked List

Difficulty: Easy
Topics: Linked List, Two Pointers, Stack, Recursion

Given the head of a slightly linked list,
return true if it is a palindrome or false otherwise

This contains a O(n) space solution. 
You add the values of nodes to a list
and iterate with 2 Pointers to see
if the list is a palindrome. 
There might be an optimization to it.

O(n) time, O(n) space solution
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rep = []
        cur = head
        while cur:
            rep.append(cur.val)
            cur = cur.next
        start = 0
        end = len(rep)-1
        flag = True
        while end > start:
            if rep[start] != rep[end]:
                flag = False
                break
            start += 1
            end -= 1
        return flag



