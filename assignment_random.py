# Crack password
import random

default_pwd = "0759"

mychar = "1234567890"
times = 0
crackpwd = ""
while True:
    temp_pwd = []
    for i in range(4):
        temp_pwd.append(random.choice(mychar))

    joinpwd = "".join(temp_pwd)
    if joinpwd == default_pwd:
        print("joinpwd:", joinpwd)
        print("default_pwd:", default_pwd)
        break
    else:
        print("Finding...", times)
        times += 1
