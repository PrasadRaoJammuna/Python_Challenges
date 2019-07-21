'''
Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate
a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple

'''
n= int(input("Enter a number to generate list and tuples:"))
l =[]

for i in range(n):
    inp = int(input('enter a number :'))
    l.append(inp)
    # we can't append an item to tuple like list
    
t = tuple(l) #converting a list into tuples.
print('Tuple:',t)
print('List:',l)

    
