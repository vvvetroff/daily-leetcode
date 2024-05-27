'''
1608. Special Array With X Elements Greater Than or Equal X

You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

The description left alot to be desired.
Essentially, is there a number x such that there are x amount of 
numbers greater than or equal to x?
O(n^2) solution initially, then looked to Neetcode for optimizations
O(n) submission.
'''

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        result = -1
        # 1st submission, O(n^2) time, O(1) space solution
        #for i in range(len(nums)+1):
        #    count = 0
        #    for j in range(len(nums)):
        #        if nums[j] >= i:
        #            count += 1
        #    if count == i:
        #        result = count
        #return result
        
        # 2nd submission, O(n) time, O(n) space solution
        count = [0 for _ in range(len(nums)+1)]
        for n in nums:
            index = min(n, len(nums))
            count[index] += 1
        Sum = 0
        for i in reversed(range(len(nums)+1)):
            Sum += count[i]
            if Sum == i:
                result = i
        return result
