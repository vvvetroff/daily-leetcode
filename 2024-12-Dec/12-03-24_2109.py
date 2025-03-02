'''
2109. Adding Space to a String

Difficulty: Medium
Topics: Array, Two Pointers, String, Simulation

You are given a 0-indexed string s
and a 0-indexed integer array spaces
that describes the indices in the original string
where spaces will be added.
Each space should be inserted before the character at the given index.

- For example, given s = "EnjoyYourCoffee" and spaces = [5, 9],
  we place spaces before 'Y' and 'C',
  which are at indices 5 and 9 respectively.
  Thus, we obtain "Enjoy Your Coffee".

Return the modified string after the spaces have been added.

Not bad
O(n+k) where k is length of spaces array
'''

from typing import List

class Solution:
  def addSpaces(self, s: str, spaces: List[int]) -> str:
    n = len(s)
    k = len(spaces)
    out = [' '] * (n+k)
    j,l = 0,0
    for i in range(n+k):
      nextSpace = spaces[l] if l < k else -1
      if j == nextSpace:
        l += 1
      else:
        out[i] = s[j]
        j += 1

    return ''.join(out)
