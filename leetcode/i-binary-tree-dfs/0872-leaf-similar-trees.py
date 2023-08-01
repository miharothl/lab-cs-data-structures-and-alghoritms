# https://leetcode.com/problems/leaf-similar-trees/
from typing import Optional, List

from _toolbox.TreeFactory import TreeFactory
from leetcode._toolbox.Tree import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def get_leafs(self, node: TreeNode, leafs) -> List[int]:

        if node is None:
            return
        else:
            # print(node.val)

            if node.left is None and node.right is None:
                leafs.append(node.val)
            self.get_leafs(node.left, leafs)
            self.get_leafs(node.right, leafs)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        root1_leafs = []
        root2_leafs = []

        self.get_leafs(root1, root1_leafs)
        self.get_leafs(root2, root2_leafs)

        if root1_leafs == root2_leafs:
            return True
        else:
            return False



solution = Solution()

root1 = TreeFactory.array_to_binary_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])
root2 = TreeFactory.array_to_binary_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])
print("Pass") if solution.leafSimilar(root1, root2) == True else print("Fail")

root1 = TreeFactory.array_to_binary_tree([1, 2, 3])
root2 = TreeFactory.array_to_binary_tree([1, 3, 2])
print("Pass") if solution.leafSimilar(root1, root2) == False else print("Fail")

"""
Problem: leaf similar trees 
Type: binary tree, dfs

Thinking:
* use dfs using recursion (stack)
* when leaf is detected append to leafs array

Complexity:
* Time: O(N1 + N2), need to visit every node
* Memory: stack is used for recursion function calls, O(N1 + N2) for unbalanced trees, for perfectly balanced tree O(log(N1) + log(N2))
"""

