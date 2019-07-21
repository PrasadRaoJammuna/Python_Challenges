# find min and max of a list
a=[]
i=0
while i<5:
    a.append(int(input('Enter a number: ')))
    i+=1
#print(a)
c=0
for i in a:
    if i<=c:
        c=i
print(c)
c=0
for i in a:
    if i>c:
        c=i
print(c)
