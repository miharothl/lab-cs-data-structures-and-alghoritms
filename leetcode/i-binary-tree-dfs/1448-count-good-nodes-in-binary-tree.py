# https://leetcode.com/problems/count-good-nodes-in-binary-tree
from _toolbox.Tree import TreeNode
from _toolbox.TreeFactory import TreeFactory


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, node: TreeNode, count: int, max_val: int) -> int:

        if node is None:
            return 0
        else:
            # print("val: {0}".format(node.val))
            # print(count)
            # print(max_val)
            if node.val >= max_val:
                max_val = node.val
                count += 1
            if node.left:
                count = self.dfs(node.left, count, max_val)
            if node.right:
                count = self.dfs(node.right, count, max_val)

        return count

    def goodNodes(self, root: TreeNode) -> int:

        count = self.dfs(root, 0, float("-inf"))
        return count


solution = Solution()

root = TreeFactory.array_to_binary_tree([3, 1, 4, 3, None, 1, 5])
print("Pass") if solution.goodNodes(root) == 4 else print("Fail")

root = TreeFactory.array_to_binary_tree([-3, 1, 4, 3, None, 1, 5])
print("Pass") if solution.goodNodes(root) == 5 else print("Fail")

root = TreeFactory.array_to_binary_tree([3, 3, None, 4, 2])
print("Pass") if solution.goodNodes(root) == 3 else print("Fail")

root = TreeFactory.array_to_binary_tree([1])
print("Pass") if solution.goodNodes(root) == 1 else print("Fail")


# 2
#  \
#   4
#   /\
# 10 8
#      /
#     4

root = TreeFactory.array_to_binary_tree([2, None, 4, 10, 8, None, None, 4])
print("Pass") if solution.goodNodes(root) == 4 else print("Fail")

root = TreeFactory.array_to_binary_tree([-1,5,-2,4,4,2,-2,None,None,-4,None,-2,3,None,-2,0,None,-1,None,-3,None,-4,-3,3,None,None,None,None,None,None,None,3,-3])
print("Pass") if solution.goodNodes(root) == 5 else print("Fail")


"""
Problem: good nodes in binary tree using dfs
Type: binary tree

Thinking:
* recursion
* if node is max or equal than all the nodes in the path before count it

Complexity:
* Time: O(N) as we need to visit all the nodes
* Memory:O(N) recursion is using stack to store the function call frames so,
    if unbalanced tree O(N),
      otherwise O(depth),
      for perfectly balanced tree O(log(N))
"""

