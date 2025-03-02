'''
1255. Maximum Score Words Formed by Letters

Difficulty: Hard
Topics: Array, String, Dynamic Programming
        Backtracking, Bit Manipulation, Bit Mask

Given a list of words, 
list of single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words formed by using the given letters 
(words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once. 
Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

Answer from Neetcode.
I think I am beginning to understand how backtracking problems are solved.
There must be a base case which shouldnt contribute to the total result
You'd initially skip (do not include) some part of the answer to see what outcome is 
You'd then see if you can actually include some part to the total.
If you can:
Then you decrement or increment something to say that you are including this as part of your answer
You get the max or min of either the result of not including that part or the result of including it
You then undo the decrement or increment; chances are that the part may or may not be included

O(2^n) since its the form of a decision tree; either include or do't 

Hopefully I can do these on my own soon...
'''

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def canconfirm(word, lettercount):
            wordCount = Counter(word)
            for c in wordCount:
                if wordCount[c] > lettercount[c]:
                    return False
            return True

        def getScore(word):
            total = 0
            for c in word:
                total += score[ord(c)-ord('a')]
            return total

        letterCount = Counter(letters)

        def recurse(i):
            if i == len(words):
                return 0
            result = recurse(i+1) # skip current word
            if canconfirm(words[i], letterCount): # include current word
                for c in words[i]:
                    letterCount[c] -= 1  # decrement all letters used
                result = max(result, getScore(words[i]) + recurse(i+1))
                for c in words[i]:
                    letterCount[c] += 1
            return result  
        return recurse(0)
