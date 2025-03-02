'''
409. Longest Palindrome

Difficulty: Easy
Topics: Hash Table, String, Greedy

Given a string s which consists of 
lowercase or uppercase letters, 
return the length of the longest palindrome
that can be built with those letters.

Letters are case sensitive. 
For example, "Aa" is not considered a palindrome.

Not the most fancy answers, but it still decent
I know of a better solution from Neetcode, but
im not gonna use it.
O(n) time
'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = Counter(s)
        flag = True
        count = 0

        for v in hm.values():
            if v % 2 == 1:
                if flag: 
                    count += v
                    flag = False
                else: 
                    count += (v-1)
            if v % 2 == 0:
                count += v
            
        return count



