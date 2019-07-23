'Remove the duplicated elements from a list'


l = [12,15,78,1,2,3,4,10,1,8,3,1,9,100,1]
print('Duplicates of 1s:',l.count(1))
count = l.count(1)

for i in range(count-1):
    l.remove(1)

print('The no.of duplicates:',l.count(1))
print(l)
