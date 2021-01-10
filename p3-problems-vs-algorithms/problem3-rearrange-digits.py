def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    assert type(input_list) is list
    assert len(input_list) > 2

    qsort(input_list)

    is_left = True

    number_a = ""
    number_b = ""

    for item in input_list:

        if is_left:
            number_a += str(item)
            is_left = not is_left
        else:
            number_b += str(item)
            is_left = not is_left

    return [int(number_a), int(number_b)]

########################################################################################################################
# begin qsort


def sort_a_bit_recursive(items, begin_idx, end_idx):

    pivot_idx = end_idx
    pivot_val = items[pivot_idx]

    next_idx = begin_idx

    while next_idx <= pivot_idx :
        next_val = items[next_idx]
        left_of_pivot = items[pivot_idx - 1]

        if next_val >= pivot_val:
            next_idx += 1
            continue

        items[next_idx] = left_of_pivot
        items[pivot_idx - 1] = pivot_val
        items[pivot_idx] = next_val

        pivot_idx -= 1

    return pivot_idx


def sort_all_recursive(items, begin_idx, end_idx):
    if end_idx <= begin_idx:
        return

    pivot_idx = sort_a_bit_recursive(items, begin_idx, end_idx)

    sort_all_recursive(items, begin_idx, pivot_idx-1)
    sort_all_recursive(items, pivot_idx+1, end_idx)


def qsort(items: list):
    assert type(items) is list

    sort_all_recursive(items, 0, len(items) - 1)


def test_qsort_helper(test_case):
    test_case_sorted = test_case.copy()
    test_case_sorted.sort(reverse=True)
    qsort(test_case)
    if test_case == test_case_sorted:
        print("Pass")
    else:
        print("Failed")


def test_qsort():
    test_qsort_helper([8, 3, 1, 7, 0, 10, 2])


def test_qsort_edge_conditions():
    test_qsort_helper([])
    test_qsort_helper([1, 0])
    test_qsort_helper([96, 97, 98])

    try:
        qsort(None)
        print('Fail')
    except AssertionError:
        print("Pass: Returns exception. Should return exception.")


def test_qsort_large_input():
    test_qsort_helper([1, 5, 3, 56, 3, 134, 65, 234, 44, 22, 4, 45, 234, 6, 3, 45, 332, 5, 3, 45, 3, 2, 4, 5, 34 , 234,
                       3, 45, 342, 2, 34, 4, 5, 96, 97, 98, 564, 875, 334, 223, 543, 654, 334, 678, 323, 234, 234])

# end qsort
########################################################################################################################


def test_rearrange_digits_helper(test_case, debug=False):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]

    if debug:
        print(test_case[0])
        print(output)

    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


def test_rearrange_digits():
    test_rearrange_digits_helper([[1, 2, 3, 4, 5], [542, 31]])
    test_rearrange_digits_helper([[4, 6, 2, 5, 9, 8], [964, 852]])


def test_rearrange_digits_edge_conditions():
    try:
        rearrange_digits(None)
        print('Fail')
    except AssertionError:
        print("Pass: Returns exception. Should return exception.")

    try:
        rearrange_digits([1])
        print('Fail')
    except AssertionError:
        print("Pass: Returns exception. Should return exception.")


def test_rearrange_digits_large_input():
    test_rearrange_digits_helper([[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9], [987654321, 987654321]])


if __name__ == "__main__":
    test_qsort()
    test_qsort_edge_conditions()
    test_qsort_large_input()

    test_rearrange_digits()
    test_rearrange_digits_edge_conditions()
    test_rearrange_digits_large_input()



