#Write a python program to create a function that accepts a string and calculate the number of upper case letters and lower case letters.

def upper_lower(string_var):
    upper,lower=0,0
    for x in string_var:
        if x.isupper():
            upper+=1
        else:
            lower+=1
    print('Upper Case Letters in Entered String :',upper,'\nLower Case Letters in Entered String :',lower)

string_var=input('Enter a String : ')

upper_lower(string_var)