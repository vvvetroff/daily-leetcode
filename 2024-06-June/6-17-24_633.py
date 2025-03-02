'''
633. Sum of Square Numbers

Difficulty: Medium
Topics: Math, Two Pointers, Binary Search

Given a non-negative integer c,
decide whether there're
two integers a and b
such that a^2 + b^2 = c

Answer from Neetcode, I have been slacking
since my trip to Florida.
O(sqrt(c))
'''

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(sqrt(c))

        while l <= r:
            sumsq = l*l + r*r
            if sumsq == c:
                return True
            elif sumsq < c:
                l += 1
            elif sumsq > c:
                r -= 1
        return False



