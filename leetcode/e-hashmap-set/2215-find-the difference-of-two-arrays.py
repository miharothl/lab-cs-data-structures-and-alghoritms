# https://leetcode.com/problems/find-the-difference-of-two-arrays/
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        set1 = set([])
        for num in nums1:
            set1.add(num)

        set2 = set([])
        for num in nums2:
            set2.add(num)

        a1 = set([])
        for num in nums1:
            if num not in set2:
                a1.add(num)

        a2 = set([])
        for num in nums2:
            if num not in set1:
                a2.add(num)

        return [list(a1), list(a2)]


solution = Solution()
nums1, nums2 = [1, 2, 3], [2, 4, 6]
print("Pass") if solution.findDifference(nums1, nums2) == [[1, 3], [4, 6]] else print("Fail")

nums1, nums2 = [1, 2, 3, 3], [1, 1, 2, 2]
print("Pass") if solution.findDifference(nums1, nums2) == [[3], []] else print("Fail")

"""
Problem: find difference in two arrays
Type: set

Thinking:
* traverse array1,2 and add elements to set1,2
* for each element in array 1 check if its in set 2, if not add to ans1
* for each element in array 2 check if its in set 1, if not add to ans2

Complexity:
* Time: iterate through array with N and M elements, O(N+M)
* Memory: creating two sets for N and M elements, in worst case scenario, where all numbers are different, O(N+M)
"""
