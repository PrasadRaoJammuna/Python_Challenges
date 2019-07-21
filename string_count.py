

l  = ['line 1 is success','success in line 2','fatal error','warning line','network error in line 5']

#print those line which has error word
#& count how many error lines are there
count=0
for i in l:
    if 'error' in i:
        print(i)
        count+=1
print('No.of lines',count)
