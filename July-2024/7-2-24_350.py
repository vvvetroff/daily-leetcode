'''
350. Intersection of Two Arrays II

Difficulty: Easy
Topics: Array, Hash Table, Two Pointers, Binary Search
        Sorting

Given two integer array nums1 and nums2,
return an array of their intersection. Each element
in the result must appear as many times as it shows
in both arrays and you may return the result in any order.

O(n+m)
'''
from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        count = Counter(nums1)

        for num in nums2:
            if num in count:
                result.append(num)
                count[num] -= 1
                if count[num] == 0:
                    del count[num]

        return result
