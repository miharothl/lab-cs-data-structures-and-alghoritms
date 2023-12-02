# https://leetcode.com/problems/path-sum-iii/
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

    def __init__(self):
        self.counter = 0


    def dfs(self, node: Optional[TreeNode], target_sum: int, values_in_path: List[int], path_results: List[List[int]], h, prefix_sum):
        if node is None:
            return

        values_in_path.append(node.val)

        # print(values_in_path)
        prefix_sum += node.val

        if (prefix_sum - target_sum) in h.keys():
            self.counter += h[prefix_sum - target_sum]
            print("COUNT: {}".format(h[prefix_sum - target_sum]))

        if prefix_sum in h.keys():
            h[prefix_sum] += 1
        else:
            h[prefix_sum] = 1

        if node.left is None and node.right is None:
            print("LEAF")
            print(values_in_path)
            path_results.append(list(values_in_path))

        self.dfs(node.left, target_sum, values_in_path, path_results, h, prefix_sum)
        self.dfs(node.right, target_sum, values_in_path, path_results, h, prefix_sum)

        values_in_path.pop()
        h[prefix_sum] -= 1

    # def subarray_sum(self, nums: List[int], k: int):
    #
    #     h = {} #prefix_sum, freq
    #     h[0] = 1
    #
    #     prefix_sum = 0
    #     count = 0
    #
    #     for num in nums:
    #         prefix_sum += num
    #
    #         if (prefix_sum - k) in h.keys():
    #             count += h[prefix_sum - k]
    #
    #         if prefix_sum in h.keys():
    #             h[prefix_sum] += 1
    #         else:
    #             h[prefix_sum] = 1
    #
    #     return count

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        path_results = []
        h = {}
        h[0] = 1

        self.counter = 0
        self.dfs(root, targetSum, [], path_results, h, 0)
        print(path_results)

        return self.counter

        # count = 0
        # for res in path_results:
        #     count += self.subarray_sum(res, targetSum)
        #
        # return count

solution = Solution()

root = TreeFactory.array_to_binary_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
targetSum = 8
expected = 3
actual = solution.pathSum(root, targetSum)
print(expected == actual)
