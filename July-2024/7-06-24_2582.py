'''
2582. Pass the Pillow

Difficulty: Easy
Topics: Math, Simulation

There are n people standing in a line labeled from 1 to n.
The first person in the line is holding a pillow initially.
Every second, the person holding the pillow passes
it to the next person standing in the line.
Once the pillow reaches the end of the line,
the direction changes, and people continue
passing the pillow in the opposite direction.

  - For example,
    once the pillow reaches the nth person
    they pass it to the n - 1th person,
    then to the n - 2th person and so on.

Given the two positive integers n and time,
return the index of the person holding the
pillow after time seconds.

O(n) initially,
O(1) figured out during my hospital visit.
'''

# test block

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # O(n) Submission
        pos = 1
        direc = 1
        while time > 0:
            if pos == n:
                direc = -1
            if pos == 1:
                direc = 1
            pos += (1 * direc)
            time -= 1

        return pos

        #O(1) Submission
        mid = n-1
        mod = time % (mid*2)
        if mod <= mid:
            return 1 + mod
        else:
            mod = time % mid
            return n - mod
