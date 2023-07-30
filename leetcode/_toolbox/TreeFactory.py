
from leetcode._toolbox.Tree import TreeNode

class TreeFactory:

    @staticmethod
    def array_to_binary_tree(arr):
        if not arr:
            return None

        nodes = [TreeNode(val) if val is not None else None for val in arr]
        root = nodes[0]
        queue = [root]
        arr_index = 1

        while queue and arr_index < len(arr):
            node = queue.pop(0)
            if arr_index < len(arr) and arr[arr_index] is not None:
                node.left = nodes[arr_index]
                queue.append(node.left)
            arr_index += 1
            if arr_index < len(arr) and arr[arr_index] is not None:
                node.right = nodes[arr_index]
                queue.append(node.right)
            arr_index += 1

        return root

    @staticmethod
    def binary_tree_to_array(root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # Remove trailing None elements from the end of the result
        while result and result[-1] is None:
            result.pop()

        return result