'''
    โครงสร้างควบคุม Control structure
    1. แบบลำดับ
        if expresstion:
            statement

    
    2. แบบเลือก
        if expression:
            statement
        else:
            statement

        
    3. แบบทำซ้ำ
'''

age = 55
height = 32
score = 80

if age > 18:
    print("Teen")

if height > 60:
    print("High")
else:
    print("Low")

if score >= 80:
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("C")
elif score >= 50:
    print("D")
else:
    print("F")

if 4>5 or 4<2:
    print(True)
else:
    print(False)

numbers_list = [1,2,3,4]
if 4 in numbers_list:
    print("IN")

print("OUT") if 5 not in numbers_list else print("IN")