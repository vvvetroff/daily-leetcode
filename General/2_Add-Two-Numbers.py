'''
2. Add Two Numbers

Difficulty: Medium
Topics: Linked List, Math, Recursion

You are given two non-empty linked lists 
representing two non-negative integers. 
The digits are stored in reverse order, 
and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, 
except the number 0 itself.

The only problem stopping em from completing it was figuring how
to actually initialize a new linked list.
Had to look to Neetcode for that
O(n) time
I'll soon do some more problems
I am just figuring out vim stuff
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        output = ListNode()
        current = output

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            v3 = v1 + v2 + carry
            carry = v3 // 10
            v3 = v3 % 10
            current.next = ListNode(v3)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next
        return output.next
