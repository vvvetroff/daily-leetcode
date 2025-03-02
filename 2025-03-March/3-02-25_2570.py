'''
2570. Merge Two 2D Arrays by Summing Values

Difficulty: Easy
Topics: Array, Hash Table, Two Pointers

You are given two 2D integer arrays nums1 and nums2.
- nums1[i] = [id_i, val_i]
  indicate that the number with the id id_i has a value equal to val_i.
- nums2[i] = [id_i, val_i]
  indicate that the number with the id id_i has a value equal to val_i.

Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one arrays
that is sorted in ascending order by id, respecting the following conditions:
- Only ids that appear in at least one of the two arrays
  should be included in the resulting array.
- Each id should be included only once
  and its value should be the sum of the values of this id in the two arrays.
  If the id does not exist in one of the two arrays,
  then assume its value in that array to be 0.

Return the resulting array. The returned array must be sorted in ascending order by id.

O(nlogn) initially, O(n) improvement
'''
from typing import List
from collections import defaultdict
class Solution:
  def mergeArraysPointer(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    output = []
    p1, p2 = 0, 0
    n1, n2 = len(nums1), len(nums2)
    while p1 < n1 and p2 < n2:
      if nums1[p1][0] == nums2[p2][0]:
        output.append([nums1[p1][0], nums1[p1][1] + nums2[p2][1]])
        p1 += 1
        p2 += 1
      elif nums1[p1][0] < nums2[p2][0]:
        output.append(nums1[p1])
        p1 += 1
      elif nums2[p2][0] < nums1[p1][0]:
        output.append(nums2[p2])
        p2 += 1
    while p1 < n1:
      output.append(nums1[p1])
      p1 += 1
    while p2 < n2:
      output.append(nums2[p2])
      p2 += 1
    return output

  def mergeArraysHash(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    sumHash = defaultdict(int)
    for pair in nums1:
      sumHash[pair[0]] = pair[1]

    for pair in nums2:
      if pair[0] in sumHash:
        sumHash[pair[0]] += pair[1]
      else:
        sumHash[pair[0]] = pair[1]

    output = []
    for (k, v) in sorted(sumHash.items()):
      output.append([k,v])
    return output

  def test(self, nums1, nums2, expected):
    print(f"Test Case : nums1 = {nums1}, nums2 = {nums2}")
    result = self.mergeArraysHash(nums1, nums2)
    print(f'\t{"PASSED" if result == expected else "FAILED : "+str(result)}')
    result = self.mergeArraysPointer(nums1, nums2)
    print(f'\t{"PASSED" if result == expected else "FAILED : "+str(result)}')

if __name__ == "__main__":
  nums1 = [[1,2],[2,3],[4,5]]
  nums2 = [[1,4],[3,2],[4,1]]
  expected = [[1,6],[2,3],[3,2],[4,6]]
  Solution().test(nums1, nums2, expected)

  nums1 = [[2,4],[3,6],[5,5]]
  nums2 = [[1,3],[4,3]]
  expected = [[1,3],[2,4],[3,6],[4,3],[5,5]]
  Solution().test(nums1, nums2, expected)
