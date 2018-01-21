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


# Lucas function

# General series function


# Test with Assert statements


def main():
    """
    Test functions using asserts.
    :return: None
    """

    print(fibonacci(8))

    for x in range(10):
        print(x, fibonacci(x))


if __name__ == "__main__":
    main()