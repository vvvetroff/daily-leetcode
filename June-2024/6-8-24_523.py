'''
523. Continuous Subarray Sum

Given an integer array nums and an integer k, 
return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

- its length is at least two, and
- the sum of the elements of the subarray is a multiple of k.

Note that:

- A subarray is a contiguous part of the array.
- An integer x is a multiple of k if there exists an
  integer n such that x = n * k. 0 is always a multiple of k.

Answer form Editorial since my original
answer turned out to be TLE (Time Limit Exceeded)
It was sort of a two pointer solution,
which does not work well with larger arrays
probably a mistake on optimization on my part
since it does seem i am "redoing" the same calculations

Since im also on vacation, i have been doing these
dailies a bit late. I have no time to think of an answer
while I am enjoying myself at the beach.
Water here in Destin, FL is nice and lovely
'''

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        if k == 1:          # edge cases
            return True

        lookup = {0: -1}
        mod = 0
        for i in range(len(nums)):
            mod = (mod + nums[i]) % k
            if mod in lookup:
                if i - lookup[mod] > 1: 
                    return True
            else:
                lookup[mod] = i

        return False
