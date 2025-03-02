'''
1442. Count Triplets That Can For Two
      Arrays of Equal XOR

Difficulty: Medium
Topics: Array, Hash Table, Math, Bit Manipulation
        Prefix Sum

Given an array of integers arr.

We want to select three indices i, j and k 
where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

    a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
    b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]

Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.

I did not know how to go about this that didnt involve
a high time complexity
Answer from Neetcode :(
I thought I was going somewhere when I connected the 2nd example
input of [1,1,1,1,1] = 10 to nCr(5,3), but that did not turn out
to be true for all inputs. It was a coincedence.
Bitwise problems make me numb in the head
'''

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr) 
        total = 0
        for i in range(n-1):
            xor = arr[i]
            for k in range(i+1, n):
                xor ^= arr[k]
                if xor == 0:
                    total += (k-i)
        return total



