# https://leetcode.com/problems/path-sum-ii/
from typing import Optional, List

from _toolbox.TreeFactory import TreeFactory


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def dfs(self, node: Optional[TreeNode], remaining_sum: int, path_nodes: List[int], path_list: List[Optional[List[int]]]):

        if node is None:
            return

        remaining_sum -= node.val
        path_nodes.append(node.val)
        # print(pathNodes)

        if node.left is None and node.right is None:

            if remaining_sum == 0:
                # print("found")
                path_list.append(list(path_nodes))

        self.dfs(node.left, remaining_sum, path_nodes, path_list)
        self.dfs(node.right, remaining_sum, path_nodes, path_list)

        path_nodes.pop()


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res = []
        self.dfs(root, targetSum, [], res)
        # print(res)
        return res


solution = Solution()


root = TreeFactory.array_to_binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
target = 22
actual = solution.pathSum(root, target)
expected = [[5, 4, 11, 2], [5, 8, 4, 5]]

print("Pass") if actual == expected else print("Fail")
