'''
    Break Continue in loop
    Break -> stop statement if expression = true
    Continue -> skip statement if expression = true
'''

i = 1
while i < 11:
    i+=1
    if i==4:
        continue
    print("Round", i)

    if i == 6:
        break