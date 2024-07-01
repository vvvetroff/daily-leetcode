'''
1550. Three Consecutive Odds

Difficulty: Easy
Topics: Array

Given an integer array arr,
return true
if there are three consecutive odd numbers in the array.
Otherwise, return false.

O(n)
I will get this monthly badge.
'''

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(2, len(arr)):
            product = arr[i] * arr[i-1] * arr[i-2]
            if product % 2 == 1:
                return True
        return False
