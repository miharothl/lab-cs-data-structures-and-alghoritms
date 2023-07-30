# https://leetcode.com/problems/binary-tree-right-side-view
from collections import deque
from typing import Optional, List

from _toolbox.Tree import TreeNode
from _toolbox.TreeFactory import TreeFactory


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        if root is None:
            return result

        next_level = deque([root])

        while next_level:
            current_level = next_level
            next_level = deque()

            while current_level:

                node = current_level.popleft()

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            result.append(node.val)

        return result


solution = Solution()


#       1
#      / \
#     2   3
#      \   \
#       5   4
root = TreeFactory.array_to_binary_tree([1, 2, 3, None, 5, None, 4])
print("Pass") if solution.rightSideView(root) == [1, 3, 4] else print("Fail")

root = TreeFactory.array_to_binary_tree([1, None, 3])
print("Pass") if solution.rightSideView(root) == [1, 3] else print("Fail")

root = None
print("Pass") if solution.rightSideView(root) == [] else print("Fail")

"""
Problem: right side view of binary tree
Type: binary tree bfs

Thinking:
* use bfs and two queues
  - queue for next level
  - queue for current level
* while next_level
  - current_level = next_level
  - next_level = deque()
  - while current_level
    - popleft
    if last node in current level append to result
  
Complexity:
* Time: O(N) as we need to visit all the nodes
* Memory:O(N/2) to hold the queue, estimating using last level of complete binary tree
"""
