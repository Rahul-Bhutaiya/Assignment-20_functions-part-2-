#Write a python program to create a function and print a list where the values are square of numbers between 1 and 30.

def square():
    print('Printing Square Between 1 and 30....\n',[x**2 for x in range(2,30)])

square()