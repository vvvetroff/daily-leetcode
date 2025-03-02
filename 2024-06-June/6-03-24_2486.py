'''
2486. Append Characters to String
        to Make Subsequence

Difficulty: Medium
Topics: Two Pointers, String, Greedy

You are given two strings s and t 
consisting of only lowercase English letters.

Return the minimum number of characters 
that need to be appended to the end of s 
so that t becomes a subsequence of s.

A subsequence is a string that can be derived 
from another string by deleting some or no 
characters without changing 
the order of the remaining characters.

This problem is extremely greedy.
The "medium" tag really threw me
off since the answer is easy.
O(n) time, O(1) space
'''

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sp, tp = 0, 0
        sn, tn = len(s), len(t)
        while sp < sn and tp < tn:
            if s[sp] == t[tp]:
                sp += 1
                tp += 1
            else:
                sp += 1
        
        return tn - tp
        
        

