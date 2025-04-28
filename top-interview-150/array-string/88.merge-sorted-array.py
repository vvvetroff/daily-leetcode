'''
88. Merge Sorted Array

Difficulty: Easy
Topics: Array, Two Pointers, Sorting

You are given two integer arrays nums1 and nums2,
sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored.
nums2 has a length of n.
'''
from typing import List
class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    a = m-1
    b = n-1
    c = m+n-1

  def test(self, nums1, m, nums2, n, expected):
    print(f"Test Case: nums1 = {nums1}, m = {m}, nums2 = {nums2}, n = {n}")
    self.merge(nums1, m, nums2, n)
    print(f'\t{"PASSED" if nums1 == expected else "FAILED : "+str(nums1)}')
      
if __name__ == "__main__":
  nums1    = [1,2,3,0,0,0]
  m        = 3
  nums2    = [2,5,6]
  n        = 3
  expected = [1,2,2,3,5,6]
  Solution().test(nums1, m, nums2, n, expected)

  nums1    = [1]
  m        = 1
  nums2    = []
  n        = 0
  expected = [1]
  Solution().test(nums1, m, nums2, n, expected)

  nums1    = [0]
  m        = 0
  nums2    = [1]
  n        = 1
  expected = [1]
  Solution().test(nums1, m, nums2, n, expected)
