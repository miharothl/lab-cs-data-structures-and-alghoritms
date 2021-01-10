def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    assert type(input_list) is list
    assert len(input_list) > 0

    return rotated_array_search_recursive(input_list, number, lower_idx=0, upper_idx=len(input_list)-1)


def is_sorted(lower_val, upper_val):
    return lower_val < upper_val


def rotated_array_search_recursive(input_list, number, lower_idx, upper_idx):

    mid_idx = (upper_idx + lower_idx) // 2

    if input_list[mid_idx] == number:
        return mid_idx
    elif lower_idx == upper_idx:
        return -1
    elif is_sorted(input_list[lower_idx], input_list[mid_idx]):
        if input_list[lower_idx] <= number <= input_list[mid_idx-1]:
            # lower half is sorted and number is in lower half
            lower_idx = lower_idx
            upper_idx = mid_idx-1
        else:
            lower_idx = mid_idx+1
            upper_idx = upper_idx
    else:
        if input_list[mid_idx+1] >= number >= input_list[upper_idx]:
            # upper half is sorted and number is in upper half
            lower_idx = mid_idx+1
            upper_idx = upper_idx
        else:
            lower_idx = lower_idx
            upper_idx = mid_idx-1

    return rotated_array_search_recursive(input_list, number, lower_idx, upper_idx)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


def test_rotated_array_search():
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])


def test_rotated_array_search_edge_conditions():
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])
    test_function([[6, 7, 8, 9, 2, 3, 4], 1])

    try:
        rotated_array_search([], 0)
        print('Fail')
    except AssertionError:
        print('Pass')


def test_rotated_array_search_large_array():
    test_function([[
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50
    ], 1])


if __name__ == "__main__":
    test_rotated_array_search()
    test_rotated_array_search_edge_conditions()
    test_rotated_array_search_large_array()


