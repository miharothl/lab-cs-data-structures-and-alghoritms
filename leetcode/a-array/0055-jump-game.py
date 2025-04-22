# https://leetcode.com/problems/jump-game/
from typing import List


# topics: array, dynamic programming, greedy

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_jump = 0

        for i, jump in enumerate(nums):
            if i > max_jump:
                return False

            max_jump = max(max_jump, jump + i)

        return True





solution = Solution()

nums = [2,3,1,1,4]
print("pass") if solution.canJump(nums) == True else print("fail")

nums = [3,2,1,0,4]
print("pass") if solution.canJump(nums) == False else print("fail")


"""
Idea:
* track how far you can jump using max_jump
* iterate through array
** if index is more than max_jump, return False
** update max_jump = max(max_jump, i + jump)
* return True

Time Complexity:
O(n) - one pass through array

Space Complexity:
O(1) - a few new variables
"""
