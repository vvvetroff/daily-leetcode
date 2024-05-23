'''
2597. The Number of Beautiful Subsets

You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

I don't like subset problems. So far, I have not understood them (coding-wise)
Sub-optimal answer from Neetcode, i'll code up an optimal solution
soon. O(2^n) 
Submitted on 5-23-24
'''

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def recurse(i, count):
            if i == len(nums):
                return 1
            result = recurse(i+1, count)
            if not count[nums[i]+k] and not count[nums[i]-k]:
                count[nums[i]] += 1
                result += recurse(i+1, count)
                count[nums[i]] -= 1
            return result

        return recurse(0, defaultdict(int)) - 1
