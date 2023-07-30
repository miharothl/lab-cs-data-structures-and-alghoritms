# https://leetcode.com/problems/container-with-most-water/
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        p0 = 0
        p1 = len(height) - 1
        area = 0

        while p1 > p0:
            area = max(area, (p1 - p0) * min(height[p0], height[p1]))

            if height[p0] < height[p1]:
                p0 += 1
            else:
                p1 -= 1

        return area

solution = Solution()
print("Pass") if solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49 else print("Fail")
print("Pass") if solution.maxArea([1, 1]) == 1 else print("Fail")

"""
Problem: container with most water
Type: two pointers

Thinking:
* Area is biggest if width is widest. So start with p0 on left and p1 on right.
* Search for higher height so move the pointer that contains lower barrier

Complexity
* Time: O(n)
* Memory: O(1)

Reference:
* https://leetcode.com/problems/container-with-most-water/solutions/3696055/c-solution-python-java-easy-understanding-two-pointer-approach/
"""
