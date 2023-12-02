# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
import math
from typing import List


class Solution:

    def __init__(self):
        self.pick = 0

    def guess(self, number):
        if number < self.pick:
            return -1
        if number == self.pick:
            return 0
        if number > self.pick:
            return 1

    def set_pick(self, pick):
        self.pick = pick

    def binary_search(self, numbers: List[bool]) -> int:
        left = 0
        right = len(numbers) - 1

        while left <= right:
            mid = int(((right - left) / 2) + left)

            res = self.guess(mid)

            if res == 0:
                return mid
            if res > 0:
                right = mid - 1
            if res < 0:
                left = mid + 1

        return -1

    def guessNumber(self, n: int, pick: int) -> int:

        numbers = [False] * n
        numbers[pick] = True

        print(numbers)

        self.set_pick(pick)

        return self.binary_search(numbers)


solution = Solution()
print(solution.guessNumber(10, 0))
print(solution.guessNumber(10, 1))
print(solution.guessNumber(10, 2))
print(solution.guessNumber(10, 3))
print(solution.guessNumber(10, 4))
print(solution.guessNumber(10, 5))
print(solution.guessNumber(10, 6))
print(solution.guessNumber(10, 7))
print(solution.guessNumber(10, 8))
print(solution.guessNumber(10, 9))
