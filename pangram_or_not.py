#Write a python program to create a function to check whether a string is a pangram or not.

def pangram(string_var):
    alphabet_string="abcdefghijklmnopqrstuvwxyz"
    for x in alphabet_string:
        if x not in string_var.lower():
            print('Not Pangram String')
            return
    else:
        print('It\'s Pangram String')

pangram('The quick brown fox jumps over lazy the dog')
