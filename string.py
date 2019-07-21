'''
Operators:
+,*,[],[:],in, not in

'''
a = 'python'
b='love'
'''
print(a+b)
print(a*2)
print(a[::])
print(a[:3])
print(a[1:4])
print(a[::2])
'''

var = 'pyTHon Is easY To Learn'
'''
print(var.capitalize())
print(var.title())
print(var.upper())
print(var.lower())
print(var.swapcase())

print(len(var))
print(max(var))
print(min(var))
print(type(var))
print(ord('a'))
print(chr(100))
'''
var ='Python a'
'''
print(var.ljust(20,'#'))
print(var.rjust(20,'#'))
print(var.center(20,'#'))

a = 'abc'
print(a.center(4,'@'))
'''

#print(var.strip())

var ='##python##lov#er##'
'''
print(var.lstrip('#'))
print(var.rstrip('#'))
print(var.strip('#'))
'''

#print(var.replace('#',''))

'''
var ='prasadjammuna007@gmail.com'

#print(var.startswith('p'))
#print(var.endswith('@gmail.com'))

l = ['india#1.1.1.1.1','usa#1.1.1.2','uk#1.1.1.4','india#1.1.1.6','usa#1.1.1.9']
for x in l:
    res = x.startswith('usa')
    if res == True:
        print(x)



a ='python python python'
print(a.count('python'))

var ='python is easy i like python  python rocks'

print(var.find('python',31,len(var)))
print(var.index('python',23,len(var))) # after index 30: we will get an error.
# Assignment
''' 
#var = 'Hi prasad! prasad is good and smart and innoscent'
#-- how to dynamic find 'prasad' automatically
'''

c=0
while c ==-1:
    var = 'Hi prasad! prasad is good and smart and innoscent'
    s ='prasad'
    var=0

    res = print(var.find('python',31,len(var)))
'''

'''
print(var.split(' '))

var = 'jp#23#20000'
res = var.split('#')
print(res)

l=['prasad','100000','USA']
res = ' '.join(l)
h= '$'.join(l)
print(h)
print(res)
'''
'''
var ='prasad123'
print(var.isalpha())
print(var.isdigit())
print(var.isalnum())
print(var.isupper())
print(var.islower())


''' 



'''
'''

var ='python is program and python is good and python'

#print(var.index('python',42,len(var)))


#print(var.find('python',3,len(var)))

count =0
for i  in range(0,len(var)):
    search = var.find('python',count,len(var))
    if search ==-1:
        break
    else:
        print(search)
    count+=search

