def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    assert type(number) is int

    return sqrt_recursive(sqrt_number=number, upper=number, lower=0)


def sqrt_recursive(sqrt_number, upper, lower):

    x = (upper - lower) // 2 + lower
    y = x * x

    x_next = x+1
    y_next = x_next * x_next

    if y < sqrt_number < y_next:
        return x
    if y == sqrt_number:
        return x

    if y > sqrt_number:
        upper = x - 1
    elif y < sqrt_number:
        lower = x + 1

    return sqrt_recursive(sqrt_number, upper, lower)


def test_sqrt():
    print("Pass" if (3 == sqrt(9)) else "Fail")
    print("Pass" if (4 == sqrt(16)) else "Fail")
    print("Pass" if (5 == sqrt(27)) else "Fail")


def test_sqrt_edge_conditions():
    print("Pass" if (0 == sqrt(0)) else "Fail")
    print("Pass" if (1 == sqrt(1)) else "Fail")

    try:
        res = sqrt(None)
        print("Fail")
    except AssertionError:
        print("Pass: Returns exception. Should return exception.")


def test_sqrt_large_numbers():
    print("Pass" if (100 == sqrt(10001)) else "Fail")
    print("Pass" if (10000 == sqrt(100000001)) else "Fail")


if __name__ == "__main__":
    test_sqrt()
    test_sqrt_edge_conditions()
    test_sqrt_large_numbers()
