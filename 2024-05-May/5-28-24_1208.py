'''
1208. Get Equal Substrings Within Budget

Difficulty: Medium
Topics: String, Binary Search, Sliding Window, Prefix Sum

You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. 
Changing the ith character of s to ith character of t costs |s[i] - t[i]| 
(i.e., the absolute difference between the ASCII values of the characters).

Return the maximum length of a substring of s that can be changed to be the same 
as the corresponding substring of t with a cost less than or equal to maxCost.
If there is no substring from s that can be changed to its corresponding substring from t, 
return 0.

This is a sliding window problem, the first of many
I've heard about some 'sliding window' thru some of my peers
but never actually knew what it is conceptually.
This answer does not make sense to me at the moment.
I'll have to research what a sliding window is.
O(n) time
'''

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        curcost = 0
        l = 0
        result = 0
        
        for r in range(len(s)):
            curcost += abs(ord(s[r])-ord(t[r]))

            while curcost > maxCost:
                curcost -= abs(ord(s[l])-ord(t[l]))
                l += 1
            
            result = max(result, r - l + 1)
        return result
