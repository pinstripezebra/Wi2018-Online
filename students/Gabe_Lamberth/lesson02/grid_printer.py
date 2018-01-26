def plus(): 
    return '+ '

def dash(num):
    return '- ' * num

def bar(num):
    return '{}{}{}'.format('|\t','|\t','|').expandtabs(num)

def printGrid(num):
    # using int essentially rounds down
    x = int(num / 2)
    # adding one accounts for the spacing needed to align 
    y = num + 1
    
    print('{}{}{}{}{}'.format(plus(),dash(x),plus(),dash(x),plus())) 
    for l in range(x): print(bar(y))
    print('{}{}{}{}{}'.format(plus(),dash(x),plus(),dash(x),plus())) 
    for l in range(x): print(bar(y))
    print('{}{}{}{}{}'.format(plus(),dash(x),plus(),dash(x),plus()))

def main():
    tstNum1 = 3
    tstNum2 = 15
    print('Printing grid with value of 3',end="\n")
    printGrid(tstNum1)
    print()
    print('Printing next grid with value of 15',end='\n')
    printGrid(tstNum2)
    
    
    
if __name__ == "__main__":
    main()