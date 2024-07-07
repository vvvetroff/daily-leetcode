'''
2181. Merge Nodes in Between Zeros

You are given the head of a linked list,
which contains a series of integers separated by 0's.
the beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's,
merge all the nodes lying in between them into a
single node whose value is the sum of all the merged nodes.
The modified list should not contain any 0's.

Return the head of the modified linked list.

Two O(n) approaches:
    Make new LList
    Modify LList in-place
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Make new Linked List
        output = ListNode()
        cur = output
        while head:
            if head.val != 0:
                newVal = 0
                while head.val != 0:
                    newVal += head.val
                    head = head.next
                cur.next = ListNode(newVal)
                cur = cur.next
            else:
                head = head.next

        # Modify in place
        cur = head

        while cur.next:
            adding = cur = cur.next
            while cur.next.val != 0:
                adding.val += cur.next.val
                cur = cur.next
            cur = cur.next
            adding.next = cur.next
        return head.next
