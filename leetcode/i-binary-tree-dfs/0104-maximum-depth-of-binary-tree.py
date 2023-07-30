# https://leetcode.com/problems/maximum-depth-of-binary-tree
from typing import Optional
from _toolbox.Tree import TreeNode
from _toolbox.TreeFactory import TreeFactory


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __max_depth(self, depth: int, node: Optional[TreeNode]):

        if not node:
            return 0
        else:
            left_depth = self.__max_depth(depth, node.left)
            right_depth = self.__max_depth(depth, node.right)

            depth = max(left_depth, right_depth) + 1

        return depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.__max_depth(0, root)


solution = Solution()

#          3
#         / \
#        9   20
#            / \
#          15   7
root = TreeFactory.array_to_binary_tree([3, 9, 20, None, None, 15, 7])
print("Pass") if solution.maxDepth(root) == 3 else print("Fail")

#          1
#           \
#            2
root = TreeFactory.array_to_binary_tree([1, None, 2])
print("Pass") if solution.maxDepth(root) == 2 else print("Fail")

"""
Problem: depth of binary tree using dfs
Type: binary tree

Thinking:
* recursively traverse the tree
* termination condition, if node not exist return 0
* go left , go right 
* depth is max(left, right) + 1

Complexity:
* Time: O(N) as we need to visit all the nodes
* Memory:O(N) recursion is using stack to store the function call frames so,
    if unbalanced tree O(N),
      otherwise O(depth),
      for perfectly balanced tree O(log(N))
"""
