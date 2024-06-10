'''
3110. Score of a String

Difficulty: Easy
Topics: String

You are given a string s. 
The score of a string is defined as 
the sum of the absolute difference
between the ASCII values of adjacent characters.

Return the score of s.

Did this before the Neetcode video was uploaded :)
O(n)
'''

class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        score = 0
        for i in range(n-1):
            score += abs(ord(s[i]) - ord(s[i+1]))
        return score



