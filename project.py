import math
from datetime import datetime

name= input('enter your name:')

def bill_cal():
    a =True
    total_price =0
    list_item_price =[]
    while a:
        print('''
            1.list of items
            2.choose item
            3.exit
        ''')

    
        choice = int(input('enter your choice:'))
        choices =[1,2,3]
        if choice in choices:
            d = {'dal':23,'oil':35,'mirchi':33}
            if choice == 1: 
                c=1
                for i,j in d.items():
                    print('\t',c,'.',i,'₹',j)
                    c+=1
            if choice == 2:
                q =True
                while q:
                    print("press 'q' to to see main menu.")
                    item = input('enter item:')
                    if item in d.keys():
                        qnt = input('enter Quantity:')
                        if qnt.isdigit():
                            
                            qnt = int(qnt)
                            price = float(d[item]*qnt)
                            list_item_price.append((item,qnt,price))
                            total_price +=price
                        else:
                            print('Invalid Input Quantity..')
                    elif item == 'q':
                        q=False

                    else:
                        print('item not present.')


            if choice == 3:
                a = False
        else:
            print('Invalid Input..Please Enter a valid input.')
    return total_price,'Thank you, Please Visit again.',list_item_price

total,msg,item_price = bill_cal()
if total !=0:
    print('\n')
    print('''
                JP Stores
            BTM,Bangalore,560076

    ''')
    print('Customer Name:',name,'\t','Date:',datetime.now())
    print(20*'==')
    #print('\n')

    for j in item_price:
        print('Item:',j[0],'\tQuntity:',j[1],' Price:',j[2])

    gst = total * 0.1
    gst = math.ceil(gst)
    print(18*'==')
    print('GST: Rs.',float(gst))
    print('Total payble amount: Rs.',float(gst+total))
    print(18*'==')
    print('🙏🙏🙏 ',msg,' 🙏🙏🙏')
else:
    print("Hey, You weren't Brought anything...Please Buy something you want.")
    bill_cal()
#l = [('dal', 3, 69.0), ('dal', 3, 69.0)]
