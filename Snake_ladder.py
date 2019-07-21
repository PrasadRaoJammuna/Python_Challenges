import random

import sys

try:
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")

target  = 50
score=1

ladder1 =10
ladder2 =6
ladder3 =15

snake1=6
snake2=8
snake3=15

color.write('Snake & Ladder Game\n',"STRING")
print('Score starts with:',score)
color.write('Ladder scores: 10,6,15 \n','STRING')
color.write('Snake scores: 6,8,15 \n',"COMMENT")

color.write('======= Good Luck ======\n','STRING')

msg ='you Win'
while True:
    if score ==target:
        color.write(msg.center(25,'#'),"STRING")
        break
    inp = input('Roll dice:')
    if inp=='d':
        dice = random.randint(1,6)
        if (score+dice)>target:
            color.write('over input dice\n',"COMMENT")
            print('Dice:',dice)
            color.write('Score:',"String")
            print(score)
            color.write('Needed Dice:',"KEYWORD")
            print((target-score))
                           
                           
        else:
            print('Dice:',dice)
            score =score+dice
            color.write('Score: ','STRING')
            print(score)

            if score==10:
                color.write("Luckky Ladder added:",'STRING')
                print(ladder1)
                score=score+ladder1
                color.write('Score:',"String")
                print(score)

            elif score==20:
                color.write("Luckky Ladder added:",'STRING')
                print(ladder1)
                score=score+ladder2
                print('score:',score)

            elif score==30:
                color.write("Luckky Ladder added:",'STRING')
                print(ladder1)
                score=score+ladder3
                color.write('Score:',"String")
                print(score)

            elif score==11:
                color.write("Unluckky Snkae swallowed:",'COMMENT')
                print(snake1)
                score=score-snake1
                color.write('Score:',"String")
                print(score)
                
            elif score==22:
                color.write("Unluckky Snkae swallowed:",'COMMENT')
                print(snake1)
                score=score-snake2
                color.write('Score:',"String")
                print(score)

            elif score==45:
                color.write("Unluckky Snkae swallowed:",'COMMENT')
                print(snake1)
                score=score-snake3
                color.write('Score:',"String")
                print(score)
            
    else:
            color.write("Wrong Input..Please press 'd' \n",'COMMENT')

 
    

                    



    


    
    
