
'''num = 10

for i in range(2,num):
    if num % i ==0:
        print('Not Prime')
        break
else:
    print('Prime')
 '''

# finding a list of prime numbers in a range
lst = int(input('Enter range:'))
          
prime_list =[]

for i in range(2,lst):
    prime =True
    for j in range(2,i):
        if i%j==0:
            prime=False
    if prime:
        prime_list.append(i)
print(prime_list)
        
