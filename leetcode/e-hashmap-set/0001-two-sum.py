# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, num in enumerate(nums):

            complement = target - num

            if complement in seen:
                return seen[complement], i

            seen[num] = i


solution = Solution()

nums = [2,7,11,15]
target = 9
print("pass") if solution.twoSum(nums, target) == (0, 1) else print ("fail")

nums = [3, 2, 4]
target = 6
print("pass") if solution.twoSum(nums, target) == (1, 2) else print ("fail")

nums = [3,3]
target = 6
print("pass") if solution.twoSum(nums, target) == (0, 1) else print ("fail")

"""
Idea:

Time:
O(N) - one pass through array

Space:
O(N) - hash map, wost case all elements are mapped
"""