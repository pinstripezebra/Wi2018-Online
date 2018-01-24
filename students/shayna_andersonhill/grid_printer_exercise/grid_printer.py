#!/usr/bin/python3
#Shayna Anderson-Hill
#Script to write a function that draws a grid
#01-22-2018

plus = '+'
minus = '-'
space = ' '
line = '|'

#print(plus, (minus+space)*4,plus, (minus+space)*4,plus)
#print(line, space*8, line, space*8, line)
#print(line, space*8, line, space*8, line)
#print(line, space*8, line, space*8, line)
#print(line, space*8, line, space*8, line)
#print(plus, (minus+space)*4,plus, (minus+space)*4,plus)
#print(line, space*8, line, space*8, line)
#print(line, space*8, line, space*8, line)
#print(line, space*8, line, space*8, line)
#print(line, space*8, line, space*8, line)
#print(plus, (minus+space)*4,plus, (minus+space)*4,plus)

#Create function to print grid customized by input value n

#Question: Is there a way to force the input to be an integer?
def horizontals(n):
    print(plus, (minus+space)*(n-1) + minus,plus, (minus + space)*(n-1)+
            minus,plus)

def print_grid(n):
    horizontals(n)
    for i in range(n):
        print(line, space*((n*2)-1), line, space*((n*2)-1), line)
    horizontals(n)
    for i in range(n):
        print(line, space*((n*2)-1), line, space*((n*2)-1), line)
    horizontals(n)

#Test
print_grid(1)
print_grid(2)
print_grid(3)
print_grid(4)





