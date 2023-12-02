# https://leetcode.com/problems/maximum-average-subarray-i
from typing import List


class Solution:

    # def calculateAverage(self, nums: List[int]):
    #     count = 0
    #     sum = 0
    #     for num in nums:
    #         sum += num
    #         count += 1
    #     return sum/count

    def findMaxAverage(self, nums: List[int], k: int) -> float:

        w0 = 0
        w1 = w0 + k

        # max_average = float("-inf")
        max_sum = float("-inf")

        while w1 <= len(nums):
            window = nums[w0:w1]
            # max_average = max(max_average, self.calculateaverage(window))
            max_sum = max(max_sum, sum(window))

            w0 += 1
            w1 += 1

        return max_sum / k


solution = Solution()

nums, k = [1, 12, -5, -6, 50, 3], 4
print("Pass") if solution.findMaxAverage(nums, k) == 12.75 else print("Fail")

nums, k = [5], 1
print("Pass") if solution.findMaxAverage(nums, k) == 5 else print("Fail")
