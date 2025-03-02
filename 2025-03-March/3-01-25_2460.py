'''
2460. Apply Operations to an Array

Difficulty: Easy
Topics: Array, Two Pointers, Simulation

You are given a 0-indexed array nums of size n consisting of non-negative integers.
You need to apply n - 1 operations to this array where,
in the ith operation (0-indexed),
you will apply the following on the ith element of nums:

- If nums[i] == nums[i + 1],
  then multiply nums[i] by 2 and set nums[i + 1] to 0. 
  Otherwise, you skip this operation.

After performing all the operations, shift all the 0's to the end of the array.

- For example,
  the array [1,0,2,0,0,1] after shifting all its 0's to the end,
  is [1,2,1,0,0,0].

Return the resulting array.

Note that the operations are applied sequentially, not all at once.

O(n)
'''
from typing import List
class Solution:
  def applyOperations(self, nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(n-1):
      if nums[i] == nums[i+1]:
        nums[i] *= 2
        nums[i+1] = 0
    zero = 0
    for i in range(n):
      if nums[i] != 0:
        nums[i], nums[zero] = nums[zero], nums[i]
        zero += 1
    return nums

  def test(self, nums, expected):
    print(f"Test Case: {nums}")
    self.applyOperations(nums)
    print(f'{nums} | {"PASSED" if nums == expected else "FAILED"}\n')

if __name__ == "__main__":
  nums = [1,2,2,1,1,0]
  expected = [1,4,2,0,0,0]
  Solution().test(nums, expected)

  nums = [0,1]
  expected = [1,0]
  Solution().test(nums, expected)
