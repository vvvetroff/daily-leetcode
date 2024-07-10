'''
1518. Water Bottles

Difficulty: Easy
Topics: Math, Simulation

There are numBottles water bottles that are initially full of water.
You can exchange numExchange empty water bottles from the market
with one full water bottle.

The operation of drinking a full water bottle
turns it into an empty bottle.

Given the two integers numBottles and numExchange,
return the maximum number of water bottles you can drink.

Not my answer, as I did this very late.
Has something to do with Geometric Series i believe
O(1) amazingly
'''

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return (numBottles*numExchange-1)//(numExchange-1)

