# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
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

    # def dfs(self, node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    #
    #     if node is None:
    #         return None
    #     else:
    #
    #         if node.val == val:
    #             return node
    #         if node.left:
    #             found = self.dfs(node.left, val)
    #             if found:
    #                 return found
    #         if node.right:
    #             found = self.dfs(node.right, val)
    #             if found:
    #                 return found
    #
    #     return None


    def recurse(self, node: Optional[TreeNode], search: int) -> Optional[TreeNode]:

        if not node:
            return None

        if search < node.val:
            return self.recurse(node.left, search)
        elif search > node.val:
            return self.recurse(node.right, search)
        else:
            return node

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.recurse(root, val)


solution = Solution()

root = TreeFactory.array_to_binary_tree([4, 2, 7, 1, 3])

print("Pass") if TreeFactory.binary_tree_to_array(solution.searchBST(root, 2)) == [2,1,3] else print("Fail")
print("Pass") if TreeFactory.binary_tree_to_array(solution.searchBST(root, 5)) == [] else print("Fail")

"""
Problem: search in binary search tree
Type: binary search tree

Thinking:
* is search val is more then node go right otherwise go left
* recursion

Complexity:
* Time: O(H), O(log(N)) insert, 
* Memory:O(H), O(log(N)) recursion is using stack to store the function call frames
"""

