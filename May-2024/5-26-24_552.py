'''
552. Student Attendance Record II

An attendance record for a student can be represented as a string where 
each character signifies whether the student was absent, late, or present on that day. 
The record only contains the following three characters:

- 'A': Absent.
- 'L': Late.
- 'P': Present.

Any student is eligible for an attendance award if they meet both of the following criteria:

- The student was absent ('A') for strictly fewer than 2 days total.
- The student was never late ('L') for 3 or more consecutive days.

Given an integer n, return the number of possible 
attendance records of length n that make a student eligible for an attendance award. 
The answer may be very large, so return it modulo 10^9 + 7.

Initially I had a naive recursive approach where i'd loop 3 times
to include all possible attendance states, but the loop did not work
I did not need the for loop. 
I believe this is O(n) bc of memoization.
3-dimensional DP is quite something, but it was probably the easiest
3-D DP problem i've come across, in retrospect.
I don't like thinking about DP problems, but they are not that bad
once you solve them.
Runtime is garbage bc its Top-Down DP (recursive): 6300ms
There is probably some way to convert this down to Bottom-Up
to get a better Runtime
The lil "MOD" requirement, while necesary, sucks
'''

class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[[-1 for _ in range(2)] for _ in range (3)] for _ in range(n+1)]

        def recurse(n, total_lates, total_abs):
            if n <= 0:
                return 1

            if dp[n][total_lates][total_abs] != -1:
                return dp[n][total_lates][total_abs]

            result = 0
            result += recurse(n-1, 0, total_abs)

            if total_lates < 2:
                result += recurse(n-1, total_lates + 1, total_abs)
            if total_abs < 1:
                result += recurse(n-1, 0, total_abs + 1)

            dp[n][total_lates][total_abs] = result % MOD
            return dp[n][total_lates][total_abs]

        return recurse(n, 0, 0)
