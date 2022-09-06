#Write a python program to create a function that takes a list and returns a new list with the original list's unique elements.

def unique(list_var):
    return list(set(list_var))

list_var=[eval(x) for x in input('Enter Elements Separated By Comma : ').split(',')]

uniq_element_list=unique(list_var)

print('Unique Elements in Original List is',uniq_element_list)