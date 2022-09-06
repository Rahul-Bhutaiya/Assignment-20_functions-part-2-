#Write a python program to access a function inside a function.

def addition(var1,var2):
    return var1+var2

def subtraction(var1,var2):
    return var1-var2

def multiplication(var1,var2):
    return var1*var2

def division(var1,var2):
    return var1/var2

def calculator():
    print('Enter 1 For Addition\nEnter 2 For Subtraction\nEnter 3 For Multiplication\nEnter 4 For Division')
    choice=int(input('Enter Your Choice : '))
    var1,var2=int(input('Enter First Value : ')),int(input('Enter Second Value : '))
    
    match choice:
        case 1:
            print(addition(var1,var2))
        case 2:
            print(subtraction(var1,var2))
        case 3:
            print(multiplication(var1,var2))
        case 4:
            print(division(var1,var2))
        case _:
            print('Enter Valid Number....')

calculator()