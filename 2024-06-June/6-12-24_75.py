'''
75. Sort Colors

Difficulty: Medium
Topics: Array, Two Pointers, Sorting

Given an array nums with n
objects colored red, white, or blue,
sort them in-place so that objects
of the same color are adjacent,
with the colors in the order red, white, and blue.

We will use the integers
0, 1, and 2 to represent
the color red, white, and blue,
respectively.

You must solve this problem
without using the library's sort function.

Follow up: Could you come up with
a one-pass algorithm using only constant extra space?

This question made me realize
that Dijkstra did not only make
Dijkstra's Algoritm.
But in true Dutch Fashion, made an algorithm
to sort the colors of the Dutch flag

Amazing
'''


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Submission 1: O(n) time, O(n) space
        n = len(nums)
        C = [0] * 3
        output = [0] * n

        for i in range(n):
            C[nums[i]] += 1

        for i in range(1, len(C)):
            C[i] += C[i-1]

        for i in reversed(range(n)):
            output[C[nums[i]]-1] = nums[i]
            C[nums[i]] -= 1

        for i in range(n):
            nums[i] = output[i]

        # Submission 2: O(n) time, O(1) Space
        i = 0
        j = 0
        k = len(nums) - 1
        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
