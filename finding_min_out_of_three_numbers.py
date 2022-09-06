#Write a python program to create a function to find the Min of three numbers.

def minimum(list_var):
    print('Enter Three Numbers Only...') if len(list_var)>3 or len(list_var)<3 else print('Minimum Number Out of Three Numbers is ',min(list_var))

list_var=[int(x) for x in input('Enter Three Numbers Separated By Comma : ').split(',')]
minimum(list_var)