# -----------------------------------------------------------
# series.py
#  Compute the Fibonacci and Lucas series.
# -----------------------------------------------------------


def fibonacci(n):
    """
    Computes the nth value in the Fibonacci series.
    :param num: n is the desired nth value in the series
    :return: Returns the nth value in the Fibonacci series
    """
    # Lower bounds check
    if n <= 0:
        return None

    # Exit statements from recursion
    if n == 1:
        return 0
    if n == 2:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """
    Computes the nth value in the Lucas series.
    :param n: n is the desired nth value
    :return: return nth value in Lucas series
    """
    # Lower bounds check
    if n <= 0:
        return None

    # Exit statements from recursion
    if n == 1:
        return 2
    if n == 2:
        return 1

    return lucas(n-1) + lucas(n-2)

# General series function


def main():
    """
    Test functions using asserts.
    :return: None
    """

    test_data_fibonacci = [
        ( -15, None), (1, 0), (9, 21), (10, 34), (16, 610), (20, 4181), (30, 514229),
    ]

    print("Assert tests:")
    for v in test_data_fibonacci:
        print(' fibonacci, given', v[0], 'expected result', v[1])
        assert fibonacci(v[0]) ==  v[1]

    test_data_lucas = [
        (-15, None), (1, 2), (2, 1), (3, 3), (4, 4), (5, 7), (6, 11), (7, 18), (30, 1149851)
    ]

    for v in test_data_lucas:
        print(' lucas, given', v[0], 'expected result', v[1])
        assert lucas(v[0]) == v[1]


if __name__ == "__main__":
    main()