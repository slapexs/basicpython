'''
    Module date / time
    method
        - year
        - month
        - day
        - hour
        - minute
        - second
'''
import datetime

datetime = datetime.datetime.now()
print(datetime) # 2022-06-03 19:17:55.293296
print(datetime.year) # 2022
print(datetime.month) # 6
print(datetime.day) # 3

print("----------------")
print("Default format:", datetime) # Default format: 2022-06-03 19:24:35.737094
print(datetime.strftime("%x")) # 06/03/22
print(datetime.strftime("%X")) # 19:25:56
print(datetime.strftime("%c")) # Fri Jun  3 19:26:35 2022
print(datetime.strftime("%H:%M:%S %p")) # 19:29:16 PM
print(datetime.strftime("%j")) # today is day 154 from 365
print(datetime.strftime("%a %A")) # Fri Friday
print(datetime.strftime("%b %B")) # Jun June
print(datetime.strftime("%w")) # 5 -> 0 = sunday, 5 = Friday
print(datetime.strftime("%d/%m/%Y")) # 03/06/2022
