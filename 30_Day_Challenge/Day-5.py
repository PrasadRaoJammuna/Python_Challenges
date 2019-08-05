'''
During the last week of track training,

shusha achieves the following times in sec-rounds: 66,57,54,53,64,52 and 59.
found her best score.

'''
l = [66,57,54,53,64,52,59]

l.sort()
print("Best score:",max(l))

c=0
'''
for i in l:
    if c<i:
        c = i
print("Best score:",c)
'''
