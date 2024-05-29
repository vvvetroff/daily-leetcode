'''
746. Min Cost Climbing Stairs

Difficulty: Easy
Topics: Array, Dynamic Programming

You are given an integer array 'cost' 
where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0,
or the step with index 1.

Return the minimum cost to reach the top of the floor.

Another DP practice question I did while in a 
study session with Adrian. 
DP was the hardest topic covered in our Algorithms course, 
so we had to get it down.
Fortunately, most, if not all, of the DP problems were focused
on what we knew already: Knapsack, Activity Selection, so on.

This intially had a O(2^n) time,
but with DP, its O(n) time and O(n) space
'''

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [cost[0]] + [cost[1]] + [0 for i in range(len(cost)-2)] 
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-1], dp[-2])



