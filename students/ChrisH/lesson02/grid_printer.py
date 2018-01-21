# ------------------------------------
# grid_printer.py
#  draw ascii grids
# ------------------------------------

P = '+'
D = '-'
V = '|'
S = ' '

def print_grid(n):
    """ Print a 2x2 grid with size as close to 'n' total columns as possible.
    :rtype: None"""

    if n < 3:
        n = 3
    if n > 20:
        n = 20

    dash = n // 2

    h_line = P + D * dash + P + D * dash + P
    grid_body = (V + S * dash + V + S * dash + V + '\n') * dash

    print(h_line)
    print(grid_body, end = '')
    print(h_line)
    print(grid_body, end = '')
    print(h_line)


def print_grid2(box_count, box_size):
    """ Print a 'box_count x box_count' grid with each box 'box_size' units wide.
    :rtype: None"""

    if box_count <= 0 or box_size < 0:
        return

    h_line = P + ((D * box_size + P) * box_count)
    b_line = V + ((S * box_size + V) * box_count)

    for h_line_count in range(box_count + 1):      # need one more horizontal line than number of cells
        # draw horizontal lines
        print(h_line)

        if h_line_count != box_count:               # don't draw the box body after the last horizontal line
            # draw the box body
            for t in range(box_size):
                print(b_line)


def main():
    """ Test functions for grid printer
    :rtype: None
    """
    print("grid printer test - 2 by 2 grid")
    print_grid(8)
    print_grid(3)
    print_grid(20)
    print_grid(-5)
    print_grid(30)

    print("grid printer test - print_grid2")
    print_grid2(3, 4)
    print_grid2(5, 3)
    print_grid2(2, 2)
    print_grid2(2, 1)
    print_grid2(30,1)
    print_grid2(2, -5)
    print_grid2(0, 0)
    print_grid2(1,1)
    print_grid2(1,0)


if __name__ == "__main__":
    main()
