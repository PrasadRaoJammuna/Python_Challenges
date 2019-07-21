
'''
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''
'''
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

n = int(input('Enter a number:'))
print(fact(n))

'''
n = int(input('Enter a number:'))
c=1
for i in range(1,n):
    c=c*(i+1)
#print(c)
print('Factorial of {} is {}'.format(n,c))






















