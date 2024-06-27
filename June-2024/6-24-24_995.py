'''
995. Minimum Number of K Consecutive Bit Flips

Difficulty: Hard
Topics: Array, Bit Manipulation, Queue
        Sliding Window, Prefix Sum

You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray
of length k from nums and simultaneously
changing every 0 in the subarray to 1,
and every 1 in the subarray to 0.

Return the minimum number of k-bit flips
required so that there is no 0 in the array.
If it is not possible, return -1.

A subarray is a contiguous part of an array.

O(n)
'''


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        q = deque()
        result = 0
        for i in range(len(nums)):
            while q and i > q[0] + k - 1:
                q.popleft()

            if (nums[i] + len(q)) % 2 == 0:
                if i + k > len(nums):
                    return -1
                result += 1
                q.append(i)
        return result
