'''
260. Single Number III

Given an integer array nums, 
in which exactly two elements appear only once 
and all the other elements appear exactly twice. 
Find the two elements that appear only once. 
You can return the answer in any order.

You must write an algorithm 
that runs in linear runtime complexity 
and uses only constant extra space.

I was close to actually solving this on my own.
All I was missing was the code from lines 28-30!
The way I previously found a common bit was wrong.
O(n) time and O(1) space, just like the Daily asked.
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorTotal = 0
        n = len(nums)

        for i in range(n):
            xorTotal ^= nums[i]
        
        bit = 1
        while not(xorTotal & bit):
            bit = bit << 1
            
        a = 0
        for i in range(n):
            if bit & nums[i] == bit:
                a ^= nums[i]
    
        b = xorTotal ^ a
        return [a,b]
