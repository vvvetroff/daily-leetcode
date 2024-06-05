'''
1002. Find Common Characters

Difficulty: Easy
Topics: Array, Hash Table, String

Given a string array 'words',
return an array of all characters
that show up in all strings within
the words
(including duplicates)
You may return the answer in any order.

Answer kinda from Neetcode.
I watched his video after going on
a 3 hour bike ride. I didn't feel
like doing anything after that tbh.

O(n^2)
'''

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])
        output = []

        for w in words:
            current = Counter(w)
            for c in count:
                count[c] = min(count[c], current[c])
        
        for c in count:
            for _ in range(count[c]):
                output.append(c)
        
        return output



