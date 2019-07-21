

import random

otp = random.randrange(10000,99999)
print(otp)
inp = int(input('Enter your OTP:'))

if otp==inp:
    print('You are allowed')
else:
    print('You are denined')
    i=1
    while i<4:
        inp = int(input("Enter your OTP:"))
        if otp==inp:
            print("You are allowed")
        else:
            print("you have ",abs(i-3)," attempts")
            print("Please Enter correct OTP:")
        i+=1
                



