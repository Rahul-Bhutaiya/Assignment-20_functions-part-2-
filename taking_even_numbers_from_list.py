#Write a python program to create a function that prints the even numbers from a given list

def even(list_var):
    print('Even Numbers in List :',[x for x in list_var if x%2==0])

list_var=[int(x) for x in input('Enter Numbers Separated By Comma : ').split(',')]
even(list_var)