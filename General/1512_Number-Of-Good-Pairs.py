'''
1512. Number of Good Pairs

Difficulty: Easy
Topics: Array, Hash Table, Math, Counting

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

O(n^2): just iterate just iterate thru all possible pairs 
        and check for the condition: if nums[i]==nums[j] and (i < j):

O(n): With the given condition/constraint, it is asking for 'unique' pairs
        Mathematically, this is done with "N choose 2", which can be
        broken down to: n(n-1)/2
        Given n numbers, how many ways can you choose 2 numbers for a pair
        nCr returns unique combinations of such
        
I found out the use of nCr by noticing a pattern between the amount of a number
and how many pairs are generated from it.

Count = 2 -> 1 Pair
Count = 3 -> 3 Pairs
Count = 4 -> 6 Pairs
Count = 5 -> 10 Pairs
Count = 6 -> 15 Pairs
Count = 7 -> 21 Pairs
Count = 8 -> 28 Pairs
so on...

I should have seen this coming, but I looked to StackOverflow for 
a math formula to generate unique pairs. it was nCr...
So much for a semesters worth of Probability... lol xD
 
I'm glad I came to this conclusion on my own tho
'''

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # O(n^2) submission
        count = 0 
        for i in range(len(nums)-1):
            j = i
            for j in range(len(nums)): 
                if nums[i]==nums[j] and (i < j):
                    count += 1
        return count 

        # O(n) submission
        count = 0
        numCount = Counter(nums) # O(n) generation; pretty busted
        for k in numCount:
            v = numCount[k]      # how many of number k is there
            count += (v * (v - 1)) // 2 # v choose 2
        return count
