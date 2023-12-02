from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = 0
        count = 0

        h = {} #, prefix_sum, frequency
        h[0] = 1

        for num in nums:
            prefix_sum += num

            if (prefix_sum - k) in h.keys():
                count += h[prefix_sum - k]

            if prefix_sum in h.keys():
                h[prefix_sum] += 1
            else:
                h[prefix_sum] = 1

        return count


solution = Solution()

nums = [1, 1, 1]
k = 2
expected = 2
actual = solution.subarraySum(nums, k)
print(expected == actual)

nums = [1, 2, 3]
k = 3
expected = 2
actual = solution.subarraySum(nums, k)
print(expected == actual)

nums = [-2, 1, 2, -2, 5, -2, 1]
k = 3
expected = 5
actual = solution.subarraySum(nums, k)
print(expected == actual)

