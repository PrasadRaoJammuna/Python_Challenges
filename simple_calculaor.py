a = int(input('Enter a number for a:'))
b = int(input('Enter a number for b:'))
while True:
    print('''
1.add
2.subtract
3.multiply
4.division
5.quit
''')
    action = int(input('Tell me your action:'))
    if action ==1:
        print('The sum of a and b is:',a+b)
    elif action ==2:
        print('The subtraction of a and b is:',a-b)
    elif action ==3:
        print('The Multiplication of a and b is:',a*b)
    elif action ==4:
        print('The division of a and b is:',a/b)
    elif action ==5:
        quit()

    else:
        print('Sorry! there is no action')



    
