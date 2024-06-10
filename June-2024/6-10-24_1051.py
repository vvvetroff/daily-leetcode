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
O(n) time, O(n+k) space
instead of O(nlogn) time
'''


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        k = max(heights)
        n = len(heights)
        C = [0] * (k+1)
        expected = [0] * n
        indices = 0

        for i in range(n):
            C[heights[i]] += 1

        for i in range(2, k+1):
            C[i] = C[i] + C[i-1]

        for i in reversed(range(n)):
            expected[C[heights[i]]-1] = heights[i]
            C[heights[i]] -= 1

        for i in range(n):
            if expected[i] != heights[i]:
                indices += 1

        return indices
