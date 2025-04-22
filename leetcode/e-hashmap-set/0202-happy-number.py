# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:

            if n in seen:
                return False

            seen.add(n)
            print(seen)

            squares = [int(digit)**2 for digit in str(n)]
            n = sum(squares)

        return True

solution = Solution()

n = 19
print("pass") if solution.isHappy(n) == True else print("fail")

n = 4
print("pass") if solution.isHappy(n) == False else print("fail")

"""
Idea:
Need to detect cycle, either
* using hashmap or set
* using two pointers (Floyd's Cycle Detection) 

Time:
* need to reduce number of digits while in the cycle
* to reduce number of digits O(log(d)) where d is number of digits in a loop
* cycle it turns out that most of the cycles are detected in less then 250 steps

O(log n per iterations x O(1) iterations = O(log n)

Space:
O(1) in practice as we store 999 = 9**2 + 9**2 + 9**2 = 81 + 81 + 81 = 243 numbers
"""