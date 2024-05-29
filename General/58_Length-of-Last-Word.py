'''
58. Length of Last Word

Difficulty: Easy
Topics: String

Given a string s consisting of words and spaces,
return the length of the last word in the string.

A word is a maximal substring consisting of 
non-space characters only.

O(n) time
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = len(s)-1
        count = 0
        while index >= 0:
            if s[index] != " ":
                count += 1
                if s[index-1] == " ":
                    break
            index -= 1
        return count



