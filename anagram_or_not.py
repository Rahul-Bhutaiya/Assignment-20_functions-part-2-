#Write a python program to create a function to check whether a string is an anagram or not.

def anagram(string_var1,string_var2):
    if len(string_var1)==len(string_var2):
        for x in string_var1:
            if x.lower() not in string_var2.lower():
                print('Not Anagram String')
                return
        else:
            print('It\'s Anagram String')
    else:
        print('Not Anagram String')

def anagram_method2(string_var1,string_var2):
    if sorted(string_var1.lower())==sorted(string_var2.lower()):
        print('It\'s Anagram String')
    else:
        print('Not Anagram String')

        
str1=input('Enter First String : ')
str2=input('Enter Second String : ')

anagram_method2(str1,str2)