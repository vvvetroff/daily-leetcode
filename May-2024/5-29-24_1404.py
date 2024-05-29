'''
1404. Number of Steps to Reduce a Number
    in Binary Representation to One.

Difficulty: Medium
Topics: String, Bit Manipulation

Given the binary representation of an integer as a string s, 
return the number of steps to reduce it to 1 under the following rules:

 - If the current number is even, you have to divide it by 2.

 - If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.

This one was really is to implement (IN PYTHON).
I thought it was easy to convert my python code to C.
Only to find that the input can be as long as 500 chars long.
My code bitwise shifts left based on were bit '1' is. 
Since inputs can be massive, see my code just work and get
accepted is just miraculous and pretty dangerous.
With my code, C does not have the capacity
to bit shift 64+ chars.
Which is probably why the memory takes 16.6 MB.
(This is meaningless since I just checked Neetcode
and he also had around 16.5 MB memory usage; thats just python ig)

Nevertheless, I can see why people think
it should be an 'easy' since most people
code in python. 

O(n) time
'''

class Solution:
    def numSteps(self, s: str) -> int:
        number = 0
        n = len(s)
        for i in range(len(s)-1, -1, -1):
            if int(s[i]):
                shift = n - i - 1
                number += 1 << shift

        steps = 0
        while number != 1:
            if number % 2 == 0:
                number = number // 2
            else:
                number += 1
            steps += 1
            
        return steps



