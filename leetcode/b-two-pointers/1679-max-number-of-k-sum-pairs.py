# https://leetcode.com/problems/max-number-of-k-sum-pairs/
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        p1, p2 = 0, len(nums) - 1

        count_operations = 0

        while p1 < p2:
            a = nums[p1]
            b = nums[p2]

            c = a + b

            if c == k:
                p1 += 1
                p2 -= 1
                count_operations += 1
            elif c > k:
                p2 -= 1
            else:
                p1 += 1

        return count_operations


solution = Solution()
print("Pass") if solution.maxOperations([1, 2, 3, 4], 5) == 2 else print("Fail")
print("Pass") if solution.maxOperations([3, 1, 3, 4, 3], 6) == 1 else print("Fail")

"""
Problem: max number of k-sum pairs
Type: two pointers

Thinking:
* sort array of numbers by using [].sort()
* two pointers, from left and right
  * p1, p2 = 0, len(nums) - 1 
* check nums[p1] + nums[p2]
  * if == move both pointers
  * if > k move right pointer
  * if < k move left pointer

Complexity:
* Time: 1. we need to sort array
          O(N*log(N)) N is number of items in the string
        2. traverse array once
          0(N)
        Total O(N*log(N))
* Space:
        depends on the sort algorithm
            Timsort O(n*log(n)) 
"""
