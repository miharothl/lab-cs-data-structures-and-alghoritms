# https://leetcode.com/studyplan/leetcode-75/
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        altitude = 0
        max_alt = 0

        for step in gain:
            altitude += step
            max_alt = max(altitude, max_alt)

        return max_alt


solution = Solution()

gain = [-5, 1, 5, 0, -7]
print("Pass") if solution.largestAltitude(gain) == 1 else print("Fail")

"""
Problem: find the highest altitude
Type: prefix-sum

Thinking:
* set altitude and max_altitude = 0
* traverse gains
  * calculate current altitude and update max_altitude
* return max_altitude

Complexity:
* Time: 1. traverse the array
          O(N), where N is number of gains
* Space:
          O(1)
"""
