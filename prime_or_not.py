#Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.

def prime(number):
    for x in range(2,number):
        if number%x==0:
            print('Not a Prime Number')
            return #you can use break also
    else:
        print('It\'s a Prime Number')

number=int(input('Enter a Number : '))
prime(number)