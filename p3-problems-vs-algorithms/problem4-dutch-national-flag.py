def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    next_idx_0 = 0
    next_idx_2 = len(input_list)-1
    next_idx = 0

    while next_idx <= next_idx_2:

        item = input_list[next_idx]

        assert type(item) is int
        assert 0 <= item <= 2

        if item == 0:
            copy_item = input_list[next_idx_0]
            input_list[next_idx] = copy_item
            input_list[next_idx_0] = item
            next_idx_0 += 1
            next_idx += 1
        elif item == 2:
            copy_item = input_list[next_idx_2]
            input_list[next_idx] = copy_item
            input_list[next_idx_2] = item
            next_idx_2 -= 1
        else:
            next_idx += 1

    return input_list


def test_function(test_case, debug=False):
    sorted_array = sort_012(test_case)
    if debug:
        print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


def test_sort123():
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2], debug=True)


def test_sort123_edge_conditions():
    test_function([])
    test_function([0])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

    try:
        test_function(None)
        print("Fail")
    except:
        print("Pass: Returns exception. Should return exception.")

    try:
        test_function([3])
        print("Fail")
    except:
        print("Pass: Returns exception. Should return exception.")


def test_sort123_large_array():
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])


if __name__ == "__main__":
    test_sort123()
    test_sort123_edge_conditions()
    test_sort123_large_array()



