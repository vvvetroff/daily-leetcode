'''
1502. Grumpy Bookstore Owner

Difficulty: Medium
Topics: Array, Sliding Window

There is a bookstore owner that has
a store open for n minutes.
Every minute, some number of customers enter the store.
You are given an integer array customers of length n
where customers[i] is the number of the customer
that enters the store at the start of the ith minute
and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.
You are given a binary array grumpy
where grumpy[i] is 1 if the bookstore owner is grumpy
during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy,
the customers of that minute are not satisfied,
otherwise, they are satisfied.

The bookstore owner knows a secret technique
to keep themselves not grumpy
for minutes consecutive minutes,
but can only use it once.

Return the maximum number of customers
that can be satisfied throughout the day.

O(n)
'''


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = 0
        win, maxwin = 0, 0
        good = 0
        for r in range(len(customers)):
            if grumpy[r]:
                win += customers[r]
            else:
                good += customers[r]

            if r - l + 1 > minutes:
                if grumpy[l]:
                    win -= customers[l]
                l += 1
            maxwin = max(win, maxwin)
        return good + maxwin
