'''
1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

Difficulty: Easy
Topics: Two Pointers, String, String Matching

Given a sentence that consists of some words separated by a single space,
and a searchWord, check if searchWord is a prefix of any word in sentence.

Return the index of the word in sentence (1-indexed)
where searchWord is a prefix of this word.
If searchWord is a prefix of more than one word,
return the index of the first word (minimum index).
If there is no such word return -1.

A prefix of a string s is any leading contiguous substring of s.

Coding in Python feels like cheating
Surprisingly O(n)
'''

class Solution:
  def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
    words = sentence.split()
    n = len(words)
    k = len(searchWord)
    for i in range(n):
      word = words[i]
      if searchWord == word[:k]:
        return i + 1
    return -1
