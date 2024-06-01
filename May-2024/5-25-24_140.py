'''
140. Word Break II

Difficulty: Hard
Topics: Array, Hash Table, String
        Dynamic Programming, Backtracking
        Trie, Memoization

Given a string s and a dictionary of strings wordDict, 
add spaces in s to construct a sentence
where each word is a valid dictionary word.
Return all such possible sentences in any order.

Note that the same word in the dictionary 
may be reused multiple times in the segmentation.

Answer from Neetcode, used my TTT for it
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        def recurse(i):
            if i == len(s):
                result.append(" ".join(current))
                return result
            for j in range(i, len(s)):
                w = s[i:j+1]
                if w in wordDict:
                    current.append(w)
                    recurse(j+1)
                    current.pop()
        
        current = []
        result = []
        recurse(0)
        return result



