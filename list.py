'''
    Non primitive : List
'''
empty = []
numbers = [1, -2, 3.0, "4", True]
print(numbers) # [1, -2, 3.0, "4", True]
print(numbers[2]) # 3.0
print(numbers[-2]) # 4
print(numbers[2:4]) # [3.0, '4'] 
print(numbers[2:]) # [3.0, '4', True]

# Constructor
users = list(["Jenny", "Rose", "xooxs"]) 
print(users) # ["Jenny", "Rose", "xooxs"]

'''
    การแก้ไขข้อมูล
'''
scores = [34, 56, 30, 89, 100]
print(scores) # [34, 56, 30, 89, 100]
scores[2] = 77
print(scores) # [34, 56, 77, 89, 100]


'''
    Loop
'''
numbers1 = [11, 22, 33, 44, 55]
for i in numbers1:
    print(i)

if 22 in numbers1:
    print("IN")
else:
    print("NOT")


'''
    function นับความยาวของ List
    len(list)
'''
numbers2 = [31, 42, 53, 64]
print(len(numbers2)) # 4


'''
    function การเพิ่ม/ลบ ข้อมูล
        เพิ่มข้อมูล
            .append(value) -> เพิ่มต่อหลังสุด
            .insert(index, value) -> แทรกข้อมูลลงตำแหน่งที่กำหนด

        ลบข้อมูล
            .remove(value) -> ลบข้อมูลที่ตรงกับ value 
            .pop() -> ลบข้อมูลหลังสุด
            del listnme[index] -> ลบข้อมูลโดยระบุตำแหน่ง
            del listname -> ลบ list ทิ้ง
'''

numbers3 = [1,2,3,4,5,6]
print("Default ->", numbers3) # [1,2,3,4,5,6]
numbers3.append(7)
print("Append 7 ->", numbers3) # [1,2,3,4,5,6,7]
numbers3.insert(1, 9)
print("Insert 7 into index 1 -> ", numbers3) # [1,9,2,3,4,5,6,7]
numbers3.remove(5)
print("Remove every 5 in list ->", numbers3) # [1,9,2,3,4,6,7]
numbers3.pop()
print("Delete last index -> ", numbers3) # [1,9,2,3,4,6]
del numbers3[3]
print("Delete value in index 3 -> ", numbers3) # [1,9,2,4,6]
numbers3.clear()
print("Delete all value in list -> ", numbers3) # []


'''
    คัดลอกข้อมูลจาก List
    .copy() -> คัดลอกสมาชิกทั้งหมดใน List
'''

users1 = ["Jan", "Ryujin", "Yuna"]
users2 = []
print(users1) # ["Jan", "Ryujin", "Yuna"]
print(users2) # []
users2 = users1.copy()
print(users2) # ["Jan", "Ryujin", "Yuna"]


'''
    รวมข้อมูลจากหลาย List
    List1 + List2 = NewList
    .extened(list) -> เพิ่มข้อมูลจาก List ใหม่ไปยัง List เดิม
'''
users3 = ["user01", "user02", "user03"]
age = [12, 13, 14]
print(users3) # ["user01", "user02", "user03"]
print(age) # [12, 13, 14]
result_users = users3+age
print(result_users) # ['user01', 'user02', 'user03', 12, 13, 14]

users4 = ["user04", "user05", "user06"]
print(users4) # ["user04", "user05", "user06"]
users4.extend(age)
print(users4) # ['user04', 'user05', 'user06', 12, 13, 14]


'''
    นับจำนวนสมาชิก
    .count(value) -> นับว่ามี Value นี้กี่ตัวใน List
'''
age1 = [11,12,12,13,12,14,15]
print(age1.count(12)) # 3