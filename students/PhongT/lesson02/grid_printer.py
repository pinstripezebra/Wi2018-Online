"""
Lesson 02
Grid Printer Exercise
"""
from __future__ import print_function


def printHead(numbar, size):
    for x in range(1,size+1):
        print ('+', numbar * '- ', end = "")
    print ('+')
    return None

def printBar(numbar, size):
    for x in range (1,size+1):
        print('|', numbar * 2 * ' ', end = "")
    print('|')
    return None

def printGrid(numbar):
    """
    Print 2x2 grid
    :param n: number of grid cell bar
    :return: N/a
    """
    size = 2
    grid(size, numbar)
    return None


def printGrid2(size, numbar):
    """
    Draw grid with a specified number of rows and columns
    :param size: number of row and column
    :param numbar: number of grid cell bar
    :return:
    """
    grid(size, numbar)
    return None


def grid(size, numbar):
    """
    Draw grid with a specified number of rows and columns
    :param size: number of row and column
    :param numbar: number of grid cell bar
    :return:
    """
    printHead(numbar, size)
    for x in range(1, size+1):
        for y in range(1,numbar+1):
            printBar(numbar, size)
        printHead(numbar, size)
    return None


if __name__ == "__main__":
    printGrid(5)
    printGrid(3)

    printGrid2(3, 4) # (three rows, three columns, and each grid cell four “units” in size)
    printGrid2(5, 3)
