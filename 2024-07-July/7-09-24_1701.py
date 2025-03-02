'''
1701. Average Waiting Time

Difficulty: Medium
Topics: Array, Simulation

There is a restaurant with a single chef.
You are given an array customers, where customers[i] = [arrival, time]:

  - arrival @ i is the arrival time of the ith customer.
    The arrival times are sorted in non-decreasing order.

  - time @ i is the time needed to prepare the order
    of the ith customer.

When a customer arrives,
he gives the chef his order,
and the chef starts preparing it once he is idle.
The customer waits till the chef finishes preparing his order.
The chef does not prepare food for more than one customer
at a time. The chef prepares food for customers
in the order they were given in the input.

Return the average waiting time of all customers.
Solutions within 10^5 from the actual answer are
considered accepted.

I guess why it is a medium,
but once the intuition is grasped,
the problem is ez
O(n)
'''
from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait = 0
        done = 0
        for arrival, time in customers:
            start = done if (arrival < done) else arrival
            done = start + time
            wait += (done - arrival)

        return wait / len(customers)
