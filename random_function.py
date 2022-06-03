'''
    Random Build in function
    import random
'''

import random

ran1 = random.random() # 0.0 - 1.0
print(ran1) # 0.8036372379070662

ran2 = random.uniform(1,10.5) # random value1 - value2
print(ran2) # 2.1563681896105042

ran3 = random.randrange(20, 30, 3) # random in range with (start, stop, step)
print(ran3)

ran4 = random.randint(0,4) # random value1 - value2 only integer
print(ran4)

users = ["Jisoo", "Lisa", "Rose", "Jenny"]
print(users[ran4])

print(users) # ['Jisoo', 'Lisa', 'Rose', 'Jenny']
random.shuffle(users) # Shuffle data in list
print(users) # ['Lisa', 'Jenny', 'Rose', 'Jisoo']
print(random.choice("QWERTYUIOP")) # R

for i in range(len("QWERTYUIO")):
    print(random.choice("QWERTYUIO"))