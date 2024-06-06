'''
78. Subsets

Difficulty: Medium
Topics: Array, Backtracking
        Bit Manipulation

Given an integer array nums of unique elements,
return all possible subsets
(the power set).

The solution set must not 
contain duplicate subsets. 
Return the solution in any order.

I'll be refering to this alot
since its the "base" subset problem
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # total possible subsets: 2^n where n is length of se
        total = []

        buffer = []
        def recurse(i):
            if i >= len(nums):
                total.append(buffer.copy())
                return
            buffer.append(nums[i])
            recurse(i+1)

            buffer.pop()
            recurse(i+1)

        recurse(0)
        return total



