# https://leetcode.com/problems/path-sum/
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

    # def dfs(self, node: Optional[TreeNode], targetSum: int, currentSum: int) -> bool:
    #
    #     if node is None:
    #         if currentSum == targetSum:
    #             return True
    #         else:
    #             return False
    #
    #     currentSum += node.val
    #
    #     res1 = self.dfs(node.left, targetSum, currentSum)
    #
    #     res2 = self.dfs(node.right, targetSum, currentSum)
    #
    #     if res1 or res2:
    #         return True
    #     else:
    #         return False

    def dfs(self, node: Optional[TreeNode], currentSum: int):
        if node is None:
            return False

        currentSum -= node.val

        if node.left is None and node.right is None:
            return currentSum == 0

        res1 = self.dfs(node.left, currentSum)
        res2 = self.dfs(node.right, currentSum)

        if res1 or res2:
            return True
        else:
            return False


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        return self.dfs(root, targetSum)


solution = Solution()

root = TreeFactory.array_to_binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
print("Pass") if solution.hasPathSum(root, 22) == True else print("Fail")

root = TreeFactory.array_to_binary_tree([1, 2, 3])
print("Pass") if solution.hasPathSum(root, 5) == False else print("Fail")

root = TreeFactory.array_to_binary_tree([])
print("Pass") if solution.hasPathSum(root, 0) == False else print("Fail")


"""
Problem: path-sum
Type: binary tree 

Thinking:
* use dfs to traverse the tree, current value = target value
* should have root-to-leaf path so
  return False if root node == None
* decrease target value by node value
* return True if current_value == 0
* return True if explore left or explore right is True, False otherwise

Complexity:
* Time: O(N)
* Memory:O(N)
"""