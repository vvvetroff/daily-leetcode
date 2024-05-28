'''
1. Two Sum

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

O(n^2) initially, O(n) submission
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # O(n^2) submission
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

        # O(n) submission
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in h and h[complement] != i:
                return i, h[complement]
