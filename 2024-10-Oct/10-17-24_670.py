'''
670. Maximum Swap

Difficulty: Medium
Topics: Math, Greedy

You are given an integer num.
You can swap two digits at most once 
to get the maximum valued number.

Return the maximum valued number you can get.

Guess who's back >:)

O(n)
'''

class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        maxI = -1
        swapi, swapj = 0, 0
        for i in range(len(num)-1, -1, -1):
            if num[i] > num[maxI]:
                maxI = i
            if num[i] < num[maxI]:
                swapi, swapj = i, maxI
        num[swapi], num[swapj] = num[swapj], num[swapi]
        return int(''.join(num))
