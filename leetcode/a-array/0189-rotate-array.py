# https://leetcode.com/problems/rotate-array/

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k = k % n

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, n - 1)

        reverse(0, k - 1)
        reverse(k, n - 1)

        return nums



    def rotate_bruteForce(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for _ in range(k):
            val = nums.pop()
            nums.insert(0, val)

        return nums



solution = Solution()


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("pass") if solution.rotate(nums, k) == [5,6,7,1,2,3, 4] else print("fail")

"""
# Idea
Rotate in place
1. Reverse the whole array
2. reverse first k elements
3. reverse the rest n-k elements

# Time Complexity
* O(n) - each reversal is linear

# Space Complexity
* O(1) - in-place, no extra space
"""


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("pass") if solution.rotate_bruteForce(nums, k) == [5,6,7,1,2,3, 4] else print("fail")

"""
# Idea
Rotate by brute force
* while _ < k
** pop last element
** insert to the front of array

# Time Complexity
* O(k * n) - each insert is O(n) as all elements need to shift

# Space Complexity
* O(1) - in-place, no extra data structures needed
"""
