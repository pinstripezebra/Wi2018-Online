"""Print a 2x2 grid, define two print_grid functions."""
# PART 1 - print a 2x2 grid, each cell 4 dashes large

plus, minus, bar, space = '+', '-', '|', ' '
numcells = 2
numdashes = 4

# construct the plus-and-dashes line, eg., + - - - - + - - - - +
plusline = ''
for i in range(numcells):
    plusline += plus + space + (minus+space)*numdashes
plusline += plus

# construct the bars-and-spaces line, eg., |         |         |
barline = ''
for i in range(numcells):
    barline += bar + space + space*2*numdashes
barline += bar

# print the grid
for i in range(numcells):
    print(plusline)
    for i in range(numdashes):
        print(barline)
print(plusline)


# PART 2 - convert the above into a function with 1 parameter

def print_grid(cellsize):
    """Print a 2x2 grid.

    cellsize: number of symbols in the top side of one cell,
              i.e. spaces ' ' and dashes '-',
              but excluding plus signs at both ends;
              number can be 0, odd or even (if even, reduced
              to the greatest odd because of the symmetry of pattern)
    Eg. print_grid(3) or print_grid(4) prints
            + - + - +
            |   |   |
            + - + - +
            |   |   |
            + - + - +
    """
    plus, minus, bar, space = '+', '-', '|', ' '
    numcells = 2
    # convert number of symbols in the top of each cell into number of dashes
    numdashes = int((cellsize-1)/2)
    # construct the plus-and-dashes line, eg., + - - - - + - - - - +
    plusline = ''
    for i in range(numcells):
        plusline += plus + space + (minus+space)*numdashes
    plusline += plus

    # construct the bars-and-spaces line, eg., |         |         |
    barline = ''
    for i in range(numcells):
        barline += bar + space + space*2*numdashes
    barline += bar

    # print the grid
    for i in range(numcells):
        print(plusline)
        for j in range(numdashes):
            print(barline)
    print(plusline)

# print_grid(0)
# print_grid(3)
# print_grid(4) #same as print_grid(3) above
# print_grid(9) #same result as in print_grid(11) in the assignment
# print_grid(15)

# PART 3 - make a 2-parameter function


def print_grid2(numcells, cellsize):
    """Print a square grid.

    numcells: number of cells in one side of the grid,
              number expected to be at least 1
    cellsize: number of dashes or bar signs in one side of the cell,
               number can be 0
    Eg. print_grid2(2, 1) prints
            + - + - +
            |   |   |
            + - + - +
            |   |   |
            + - + - +
    """
    plus, minus, bar, space = '+', '-', '|', ' '
    # construct the plus-and-dashes line, eg., + - - - - + - - - - +
    plusline = ''
    for i in range(numcells):
        plusline += plus + space + (minus+space)*cellsize
    plusline += plus

    # construct the bars-and-spaces line, eg., |         |         |
    barline = ''
    for i in range(numcells):
        barline += bar + space + space*2*cellsize
    barline += bar

    # print the grid
    for i in range(numcells):
        print(plusline)
        for j in range(cellsize):
            print(barline)
    print(plusline)

# print_grid2(1, 0)
# print_grid2(1, 1)
# print_grid2(2, 1)
# print_grid2(3, 4)
# print_grid2(5, 3)
