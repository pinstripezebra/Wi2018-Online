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







"""
print ('+', 4*'- ', sep =' ', end= '')
print ('+', end = '')
print ('+', 4*'- ', sep =' ', end= '')
print ()


def printDashes(n):
    print (n*'- ', sep =' ', end= '')

def printPlus():
    print('+', end=' ')

def printMinus():
    print('-', end=' ')

def printBar():
    print('|', end=' ')

def printSpace():
    print(' ', end=' ')

def printSpaces(n):
    print(n*' ',  sep =' ', end= ' ')

def printHead(n):
    printPlus()
    #doRepeat(n,printMinus)
    printDashes(n)

    printPlus()
    #doRepeat(n,printMinus)
    printDashes(n)
    printPlus()
    print()

def printRow():
    printBar()
    doRepeat(numBar,printSpace)
    #printSpaces(numBar)
    printBar()
    doRepeat(numBar,printSpace)
    # do_twice(printBar, doRepeat(numBar,printSpace)) // ERROR
    printBar()
    print()

# not used yet
def do_twice(g,h):
    g(), h()
    g(), h()


def doRepeat(n,f):
    for x in range (0, n):
        f()


size = 11
numBar = (size - 1)//2 # should be ok when size = even number

printHead(numBar)
doRepeat(numBar,printRow)
printHead(numBar)
doRepeat(numBar,printRow)
printHead(numBar)
"""









"""
def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end =' ')

def print_post():
    print('|        ', end=' ')

def print_beams():
    do_twice(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()
"""