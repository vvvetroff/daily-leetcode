'''
3068. Find the Maximum Sum of Node Values

Difficulty: Hard
Topics: Array, Dynamic Programming, Greedy,
        Bit Manipulation, Tree, Sorting

There exists an undirected tree with n nodes numbered 0 to n - 1. 
You are given a 0-indexed 2D integer array edges of length n - 1, 
where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree.
You are also given a positive integer k, 
and a 0-indexed array of non-negative integers nums of length n, 
where nums[i] represents the value of the node numbered i.

Alice wants the sum of values of tree nodes to be maximum, 
for which Alice can perform the following operation any number of times (including zero) on the tree:

- Choose any edge [u, v] connecting the nodes u and v, and update their values as follows:
    - nums[u] = nums[u] XOR k
    - nums[v] = nums[v] XOR k

Return the maximum possible sum of the values Alice can achieve 
by performing the operation any number of times.

Answer from Neetcode, O(nlogn)
'''

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        delta = [(n^k)-n for n in nums]
        delta.sort(reverse=True)
        result = sum(nums)

        for i in range(0, len(nums), 2):
            if i == len(nums) - 1:
                break
            sumDelta = delta[i] + delta[i+1]
            if sumDelta <= 0:
                break
            result += sumDelta
        return result



