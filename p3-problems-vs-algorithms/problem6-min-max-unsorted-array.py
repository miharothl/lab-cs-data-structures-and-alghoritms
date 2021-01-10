def get_min_max(items):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       items(list): list of integers containing one or more integers
    """
    
    assert type(items) is list 
    assert len(items) > 0

    min_value = items[0]
    max_value = items[0] 
    
    for item in items:
        assert type(item) is int

        if item < min_value:
            min_value = item

        if item > max_value:
            max_value = item
        
    return min_value, max_value


def test_get_min_max(debug=False):
    import random
    l = [i for i in range(0, 10)]
    random.shuffle(l)

    min_max = get_min_max(l)

    if debug:
        print(l)
        print(min_max)

    print("Pass" if ((0, 9) == min_max) else "Fail")


def test_get_min_max_large_input():

    import random
    l = [i for i in range(0, 100)]
    random.shuffle(l)

    print("Pass" if ((0, 99) == get_min_max(l)) else "Fail")


def test_get_min_max_edge_conditions():

    try:
        get_min_max(None)
        print('Fail')
    except AssertionError:
        print('Pass')

    try:
        get_min_max([])
        print('Fail')
    except AssertionError:
        print('Pass')

    try:
        get_min_max([1,'a'])
        print('Fail')
    except AssertionError:
        print('Pass')


if __name__ == "__main__":
    test_get_min_max(debug=True)
    test_get_min_max_edge_conditions()
    test_get_min_max_large_input()



