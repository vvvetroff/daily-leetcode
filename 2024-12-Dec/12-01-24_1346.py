'''
1346. Check If N and Its Double Exist

Difficulty: Easy
Topics: Array, Hash Table, Two Pointers, Binary Search, Sorting

Given an array arr of integers,
check if there exist two indices i and j such that:
  - i != j
  - 0 <= i, j < arr.length
  - arr[i] == 2 * arr[j]

Binary search was the most intuitive for me
O(nlogn)

I do not understand or intuit how
a Two Pointer approach would work.
The editorial doesn't show.
'''
from typing import List

class Solution:
  def checkIfExist(self, arr: List[int]) -> bool:
    n = len(arr)
    arr.sort()

    def bs(target):
      l, r = 0, n-1
      while l <= r:
        mid = (r+l) // 2
        if arr[mid] == target:
          return mid
        elif arr[mid] > target:
          r = mid - 1
        else:
          l = mid + 1
        return -1

    for i in range(n):
      index = bs(arr[i] * 2)
      if index >= 0 and index != i:
        return True
    return False
