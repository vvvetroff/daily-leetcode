'''
786. K-th Smallest Prime Fraction

Difficulty: Medium
Topics: Array, Two Pointers, Binary Search, Sorting, Heap (PQ)

You are given a sorted integer array 'arr' containing 1 and prime numbers, 
where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the
fraction arr[i] / arr[j].

Return the kth smallest fraction considered. 
Return your answer as an array of integeres of size 2, 
where answer[0] == arr[i] and answer[1] == arr[j]

Generate fraction and insert the fraction and the values to make that fraction into a heap
Extract the kth item and return it.
Heaps makes sense for this problem conceptually but it sucks
for runtime. I believe there is a binary search way of doing this
2200ms runtime (ew)
O(n^2log(n))?
'''

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n):
                frac = (arr[i]/arr[j],(arr[i], arr[j]))
                heappush(heap, frac)
        
        for _ in range(k):
            a, b = heappop(heap)[1]
        
        return [a,b]
