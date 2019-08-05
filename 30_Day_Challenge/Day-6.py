'''
The city's bus system carries 1,20,000 people each day. How many people
does the bus system carry each year.?(365days).
Solve without using */,bitwise operator or for loop

'''

n = 0
people = 120000
c=0
while n<365:
    c +=people
    n+=1

print("Total people per year:",c)

#print(120000*365)
