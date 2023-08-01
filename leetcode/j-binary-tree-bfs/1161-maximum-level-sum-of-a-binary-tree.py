# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
from collections import deque
from typing import Optional

from _toolbox.TreeFactory import TreeFactory
from leetcode._toolbox.Tree import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        next_level = deque()

        level_sums = []

        next_level.append(root)

        while next_level:
            current_level = next_level
            next_level = deque()

            sum = 0
            while current_level:
                node = current_level.popleft()
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

                sum += node.val

            level_sums.append(sum)


        max_sum = float('-inf')
        level = 0
        ans = -1
        for sum in level_sums:
            level += 1

            if max_sum < sum:
                max_sum = sum
                ans = level

        # print(level_sums)

        return ans


solution = Solution()

root = TreeFactory.array_to_binary_tree([1, 7, 0, 7, -8, None, None])
print("Pass") if solution.maxLevelSum(root) == 2 else print("Fail")

root = TreeFactory.array_to_binary_tree([989, None, 10250, 98693, -89388, None, None, None, -32127])
print("Pass") if solution.maxLevelSum(root) == 2 else print("Fail")

root = TreeFactory.array_to_binary_tree([1, 1, 0, 7, -8, -7, 9])
print("Pass") if solution.maxLevelSum(root) == 1 else print("Fail")
