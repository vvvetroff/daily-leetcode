'''
974. Subarray Sums Divisible by K

Difficulty: Medium
Topics: Array, Hash Table, Prefix Sum

Given an integer array nums and an integer k, 
return the number of non-empty subarrays 
that have a sum divisible by k.

A subarray is a contiguous part of an array.

I do not completely understand prefix things
O(n) time, O(n) space
'''


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        counting = 0
        result = 0
        for i in range(len(nums)):
            counting += nums[i]
            mod = counting % k
            if mod in prefix:
                result += prefix[mod]
            prefix[mod] += 1

        return result
