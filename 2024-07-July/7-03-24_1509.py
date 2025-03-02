'''
1509. Minimum Difference Between Largest and Smallest
    Value in Three Moves

Difficulty: Medium
Topics: Array, Greedy, Sorting

You are given an integer array nums.

In one move, you can choose one element of nums and
change it to any value.

Return the minimum difference between the largest
and smallest value of nums after performing at most
three moves.

O(nlog)
'''
import math
from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
        result = int(math.inf)

        for l in range(4):
            r = len(nums) - 4 + l
            result = min(result, abs(nums[r] - nums[l]))

        return result
