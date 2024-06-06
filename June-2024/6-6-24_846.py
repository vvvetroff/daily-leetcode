'''
846. Hand of Straights

Difficulty: Medium
Topics: Array, Hash Table, Greedy, Sorting

Alice has some number of cards 
and she wants to rearrange the cards 
into groups so that each group is of size groupSize, 
and consists of groupSize consecutive cards.

Given an integer array hand 
where hand[i] is the value written 
on the ith card and an integer groupSize, 
return true if she can rearrange the cards, 
or false otherwise.

I understood that I needed to use a
hashmap/frequency table for the cards,
and I understood that I would have to
get the minimum element each time I 
"construct" a new group. However,
I did not know how to get the "first"
element in a dictionary in python.
"Counter()" functions as a defaultdict,
where if a certain key isnt present,
the value of it defaults to 0.
Apparently, "next(iter(dictionary))" is 
the way to do it.
Had to use the Neetcode video for some hints.

I dunno how I feel about this daily,
I feel like I could have figured it out
had I knew some python knowledge

ugh
'''

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        count = dict(sorted(count.items()))

        while count:
            first = next(iter(count))
            for i in range(first, first+groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    count.pop(i)

        return True



