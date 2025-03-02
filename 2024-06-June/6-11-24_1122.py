'''
1122. Relative Sort Array

Given two arrays arr1 and arr2,
the elements of arr2 are distinct,
and all elements in arr2 are also in arr1.

Sort the elements of arr1
such that the relative ordering of items
in arr1 are the same as in arr2.
Elements that do not appear in arr2
should be placed at the end of arr1 in ascending order.

Took the easy way out since i did not want to write
Counting Sort again.
'''


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2set = set(arr2)
        count = defaultdict(int)
        end = []
        output = []

        for n in arr1:
            count[n] += 1
            if n not in arr2set:
                end.append(n)

        end.sort()

        for n in arr2:
            val = count[n]
            for _ in range(val):
                output.append(n)

        return output + end
