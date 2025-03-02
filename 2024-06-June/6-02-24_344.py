'''
344. Reverse String

Write a function that reverses a string.
The input string is given as an array of characters s.

You must do this by modifying 
the input array in-place with O(1) extra memory.

Currently on a road trip to Florida (the pan-handle)
Using my iphone hotspot to complete this daily.
This was kinda confusing since you can do this:

    s = s[::-1]

in python. ppl say it works (submission-wise)
This is O(n) time with O(1) space
'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s)-1
        m = l + r // 2
        while l <= m and r >= m:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1



