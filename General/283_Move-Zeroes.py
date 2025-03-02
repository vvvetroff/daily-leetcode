'''
283. Move Zeroes

Difficulty: Easy
Topics: Array, Two Pointers

Given an integer array nums,
move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

O(n)
'''

from typing import List
class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    zero = 0
    for i in range(n):
      if nums[i] != 0:
        nums[i], nums[zero] = nums[zero], nums[i]
        zero += 1

  def test(self, nums, expected):
    print(f"Test Case: {nums}")
    self.moveZeroes(nums)
    print(f'{nums} | {"PASSED" if nums == expected else "FAILED"}\n')

if __name__ == "__main__":
  nums = [0,1,0,3,12]
  expected = [1,3,12,0,0]
  Solution().test(nums, expected)

  nums = [0]
  expected = [0]
  Solution().test(nums, expected)
