'''
Add set of elements to a list in requred positions.


'''

l = [100,3,5,99,50]

p=[120,789,500]

count = len(p)
index = [1,3,5]

for i in range(count):
    l.insert(index[i],p[i])
    
    
    
    


print(l)
