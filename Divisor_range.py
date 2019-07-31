
inp = int(input("Enter a number: "))

divisors =[]

for i in range(1,inp+1):
    
    if inp % i==0:
        divisors.append(i)

print('divisors',divisors)
        
