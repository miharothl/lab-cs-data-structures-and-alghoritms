# https://leetcode.com/problems/same-tree/
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left)  and self.isSameTree(p.right, q.right)

tree1 = TreeFactory.array_to_binary_tree([1, 2, 3])
tree2 = TreeFactory.array_to_binary_tree([1, 2, 3])

solution = Solution()
print("pass") if solution.isSameTree(tree1, tree2) == True else print("fail")