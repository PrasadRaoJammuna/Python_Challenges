var = 'python is program python is good python ends'

'''
s=0
search = var.find('python',s,len(var))
print(search)
s=search+1
search = var.find('python',s,len(var))
print(search)
s=search+1
search = var.find('python',s,len(var))
print(search)
s=search+1
search = var.find('python',s,len(var))
print(search)
'''
search=0

for i in range(len(var)):
 
    search = var.find('python',search,len(var))
    if search ==-1:
        break
    print('python found at {}'.format(search))
    search+=1

          
