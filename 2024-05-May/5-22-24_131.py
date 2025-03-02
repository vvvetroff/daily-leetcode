'''
131. Palindrome Partitioning

Difficulty: Medium
Topics: String, Dynamic Programming
        Back Tracking

Given a string s, 
partition s such that every substring
of the partition is a palindrome. 
Return all possible palindrome partitioning of s.

Answer from Neetcode, used my TTT for this one
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        part = []

        def confirmPali(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i):
            if i >= len(s):
                output.append(part.copy())
                return
            for j in range(i, len(s)):
                if confirmPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return output



