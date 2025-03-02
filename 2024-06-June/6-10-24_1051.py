'''
1051. Height Checker

Difficulty: Easy
Topics: Array, Sorting, Counting Sort

A school is trying to take an
annual photo of all the students.
The students are asked to stand
in a single file line in non-decreasing
order by height.
Let this ordering be represented
by the integer array expected where
expected[i] is the expected height
of the ith student in line.

You are given an integer array heights
representing the current order that the
students are standing in.
Each heights[i] is the height
of the ith student in line (0-indexed).

Return the number of indices
where heights[i] != expected[i].

Counting Sort for the win!
CSE 3500 taught me well.
O(n+k) time, O(1) space
(C array is always the same length)
instead of O(nlogn) time
'''


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = len(heights)
        C = [0] * (101)
        indices = 0

        for i in range(n):
            C[heights[i]] += 1

        for i in range(2, len(C)):
            C[i] += C[i-1]

        for i in range(n):
            expected = heights[C[heights[i]]-1]
            C[heights[i]] -= 1
            if expected != heights[i]:
                indices += 1

        return indices
