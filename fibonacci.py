
def fib(num):
    a=0
    b=1
    if num==1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2,num):
            c =a+b
            a,b = b,c
            print(c)
            
fib(7)
