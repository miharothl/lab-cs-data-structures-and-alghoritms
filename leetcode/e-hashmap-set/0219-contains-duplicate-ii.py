# https://leetcode.com/problems/contains-duplicate-ii/
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i, num in enumerate(nums):

            if num in window:
                return True

            window.add(num)

            if len(window) > k:
                window.remove(nums[i-k])

        return False

solution = Solution()

nums = [1, 2, 3, 1]
k = 3
print("pass") if solution.containsNearbyDuplicate(nums, k) == True else print("fail")

nums = [1,0,1,1]
k = 1
print("pass") if solution.containsNearbyDuplicate(nums, k) == True else print("fail")

nums = [1,2,3,1,2,3]
k = 2
print("pass") if solution.containsNearbyDuplicate(nums, k) == False else print("fail")


"""
Idea:
* use set as a sliding window with max size k

Time:
O(n) - one pass through array

Space:
O(min(n,k))
* set is a size of k so O(k)
* worst case scenario if k is equal to n O(n)
"""



