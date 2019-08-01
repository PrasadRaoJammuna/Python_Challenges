'''
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''

inp = input("Enter name: ")

reverse = inp[::-1]

if inp == reverse:
    print('The given name is polidrome')
else:
    print("Not a polidrome")
    
