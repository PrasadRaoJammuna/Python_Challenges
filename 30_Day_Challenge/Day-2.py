# print the Below Pattern
'''
         **
         **
       ****
       ****
     ******
     ******
   ********
   ********
 **********
 **********
'''



n=10
for i in range(n+1):
    if i%2==0:
        c=0
        while c<2:
            c+=1
            #print((n-i)*' ',end=' ')
            print((n-i)*' ',i*'*')
