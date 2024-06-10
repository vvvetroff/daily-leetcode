'''
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, 
return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty 
sequence of elements within an array.

Did this cuz Neetcode recommended me to.
'''


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        counting = 0
        result = 0
        for i in range(len(nums)):
            counting += nums[i]
            if counting - k in prefix:
                result = result + prefix[counting - k]
            if counting not in prefix:
                prefix[counting] = 1
            else:
                prefix[counting] += 1

        return result
