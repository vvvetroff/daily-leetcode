'''
1823. Find the Winner of the Circular Game

Difficulty: Medium
Topics: Array, Math, Recursion, Queue, Simulation

There are n friends that are playing a game.
The friends are sitting in a circle and are numbered
from 1 to n in clockwise order.
More formally, moving clockwise from the ith friend
brings you to the (i+1)th friend for 1 <= i < n,
and moving clockwise from the nth friend brings you to the 1st friend.

The rules of the game are as follows:

 1. Start at the 1st friend
 2. Count the next k friends in the clockwise direction
    including the friend you started at.
    The counting wraps around the circle
    and may count some friends more than once.
 3. The last friend you counted leaves the circle and loses the game.
 4. If there is still more than one friend in the circle,
    go back to step 2 starting from the friend immediately
    clockwise of the friend who just lost and repeat.
 5. Else, the last friend in the circle wins the game.

Given the number of friends, n, and an integer k,
return the winner of the game.

Answer from Neetcode
'''
from collections import deque

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque()

        for i in range(1, n+1):
            q.append(i)

        while len(q) > 1:
            for i in range(k-1):
                q.append(q.popleft())
            q.popleft()
        return q[0]
