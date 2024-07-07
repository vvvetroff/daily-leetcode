'''
2058. Find the Minimum and Maximum Number of Nodes
      Between Critical Points

A critical point in a linked list is defined as either
a local maxima or a local minima.

A node is a local maxima if the current node has a
value strictly greater than the previous node and the next node.

A node is a local minima if the current node has a
value strictly smaller than the previous node and the next node.

Note that a node can only be a local maxima/minima
if there exists both a previous node and a next node.

Given a linked list head,
return an array of length 2 containing [minDistance, maxDistance]
where minDistance is the minimum distance between any two distinct critical points
and maxDistance is the maximum distance between any two distinct critical points.
If there are fewer than two critical points, return [-1, -1].

Answer from Neetcode
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def critical(prev, cur, nxt):
            return (prev.val < cur.val > nxt.val or prev.val > cur.val < nxt.val)

        prev, cur = head, head.next
        nxt = cur.next

        min_dist, max_dist = float("inf"), -1
        first_crit, prev_crit = 0, 0
        i = 1

        while nxt:
            if critical(prev,cur,nxt):
                if first_crit:
                    max_dist =  i - first_crit
                    min_dist = min(min_dist, i - prev_crit)
                else:
                    first_crit = i
                prev_crit = i
            prev, cur, nxt = cur, nxt, nxt.next
            i += 1

        if min_dist == float("inf"):
            min_dist = -1

        return [min_dist, max_dist]
