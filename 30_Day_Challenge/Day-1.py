# creating a dynamic number table for students..

'''
Tips:
-- take the input from the user
-- use string operations to get quick outputs
-- eg: 2 X 2 = 4

'''


inp =input("Enter a number to get Table:")
con= inp.isdigit()

if con :
    inp=int(inp)
    for i in range(1,11):
        print(inp,'X',i,'=',inp*i)
else:
    print('wrong Input')
    

    
