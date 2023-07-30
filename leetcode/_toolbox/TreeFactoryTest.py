from _toolbox.TreeFactory import TreeFactory


def test_tree_factory():
    #     3
    #    / \
    #   9   20
    #       / \
    #     15   7

    arr = [3, 9, 20, None, None, 15, 7]
    root = TreeFactory.array_to_binary_tree(arr)

    result = TreeFactory.binary_tree_to_array(root)

    assert arr == result
