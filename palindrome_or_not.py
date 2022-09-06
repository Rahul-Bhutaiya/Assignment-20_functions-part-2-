#Write a python program to create a function that checks whether a passed string is palindrome or not.

def palindrome(string_var):
    print('It\'s Palindrome String' if string_var==string_var[::-1] else 'Not a Palindrome String')

string_var=input('Enter a String : ')
palindrome(string_var)