"""
Lession 02
Fibonacci Series Exercise
"""


def fibonacci(n):
    """The Fibonacci Series"""
    if n <= 0:
        print("Invalid input: n must be >= 0")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """The Lucas Number"""
    if n <= 0:
        print("Invalid input: n must be >= 0")
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)



def sum_series(n, f0 = 0, f1 = 1):
    """
    :param n: nth number
    :param f0/f1: if f0=0, f1=1 then it is fibonacci. Otherwise f0=2, f1=1 then it is lucas
    :return: nth value in the series
    """
    # check if valid input for f0 and f1: either 0/1, or 2/1
    if not (f0==0 and f1==1 or f0==2 and f1==1):
        print("Invalid f0/f1 arguments")
        return None

    if n <= 0:
        print("Invalid input n: n must be > 0")
        return None
    elif n == 1:
        return f0
    elif n == 2:
        return f1
    else:
        return sum_series(n-1, f0, f1) + sum_series(n-2, f0, f1)


def testFibonacci():
    """ test fibonacci series """
    assert (fibonacci(1) == 0)
    assert (fibonacci(2) == 1)
    assert (fibonacci(3) == 1)
    assert (fibonacci(4) == 2)
    assert (fibonacci(5) == 3)
    assert (fibonacci(6) == 5)

def testLucas():
    """ test lucas series """
    assert (lucas(1) == 2)
    assert (lucas(2) == 1)
    assert (lucas(3) == 3)
    assert (lucas(4) == 4)
    assert (lucas(5) == 7)
    assert (lucas(6) == 11)

def testSumSeries():
    # test fibonacci
    assert (sum_series(1, 0, 1) == 0)
    assert (sum_series(2,     ) == 1) # test optional params with default values
    assert (sum_series(3, 0, 1) == 1)
    assert (sum_series(4, 0, 1) == 2)
    assert (sum_series(5, 0, 1) == 3)
    assert (sum_series(6, 0, 1) == 5)

    # test lucas
    assert (sum_series(1, 2, 1) == 2)
    assert (sum_series(2, 2, 1) == 1)
    assert (sum_series(3, 2, 1) == 3)
    assert (sum_series(4, 2, 1) == 4)
    assert (sum_series(5, 2, 1) == 7)
    assert (sum_series(6, 2, 1) == 11)


if __name__ == "__main__":
    # testing
    testFibonacci()
    testLucas()
    testSumSeries()
