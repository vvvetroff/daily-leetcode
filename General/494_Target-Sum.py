'''
494. Target Sum

Difficulty: Medium
Topics: Array, Dynamic Programming, Backtracking

You are given an integer array nums and an integer target.

You want to build an expression out of nums 
by adding one of the symbols '+' and '-' before 
each integer in nums and then concatenate all the integers.

 - For example, if nums = [2, 1], 
   you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.

Adrian & I were really theorizing & hypothesizing about this problem
He did the coding for this one; he had more leetcode experience
But we learned alot about DP nevertheless.
'''

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(csum, i):
            if (csum, i) in cache:
                return cache[(csum, i)]
            if i > len(nums)-1:
                if csum == target:
                    return 1    
                else:
                    return 0
            cache[(csum, i)] = dfs(csum - nums[i], i+1) + dfs(csum + nums[i], i+1)
            return cache[(csum, i)]
        
        return dfs(0, 0)



