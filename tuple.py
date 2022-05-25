'''
    Non primitive | Tuple
    Like a List but can not edit value
'''
tup1 = (1, 3.14, True, "Apple")
print(tup1) # (1, 3.14, True, 'Apple')

# Constructor
tup2 = tuple((1, 3.14,"Hi", True))
print(tup2) # (1, 3.14, 'Hi', True)
print(tup1[0]) # 1
print(tup2[:3]) # (1, 3.14, 'Hi')
print(tup2[-1]) # True
print(tup2[2:]) # ('Hi', True)
print(tup1[-3:-1]) # (3.14, True)

'''
    How to edit value in tuple!!
    1. Convert tuple to list
'''
person = (1, "Ryujin", "Single")
print(type(person)) # tuple
list_person = list(person)
print(list_person) # [1, 'Ryujin', 'Single']
print(type(list_person)) # list
person_con = tuple(list_person)
print(person_con) # (1, 'Ryujin', 'Single')

'''
    เข้าถึงข้อมูลด้วย Loop
    for i in tup:
        statement

    in keyword
    if i in tup:
        statement
'''
for i in person:
    print(i)

if 1 in person:
    print("Yes")
else:
    print("No")


'''
    นับสมาชิกด้วย len
    len()
'''
members = ("Jenny", "Rose", "Lisa", "Jisoo")
print(members) # ('Jenny', 'Rose', 'Lisa', 'Jisoo')
print(len(members)) # 4
for i in range(len(members)):
    print(members[i])

'''
    การสร้างและเพิ่มข้อมูล
    x = ("Hello") -> string
    y = ("Hello", ) -> tuple
    
    tuple + tuple = tuple
'''
empty_tuple = ("Hello")
print(empty_tuple) # "Hello"
print(type(empty_tuple)) # str
members1 = ("Jenny", "Rose", "Lisa")
jisoo = "Jisoo"
# members1 = members1+jisoo -> Error

members1 = members1+tuple(jisoo)
print(members1) # ('Jenny', 'Rose', 'Lisa', 'J', 'i', 's', 'o', 'o')
# Join tuple
members2 = ("Ryujin", "Yuna", "Yeji", "Lia")
chaeryeong = "Chaeryeong"
members2 = members2+(chaeryeong, )
print(members2) # ('Ryujin', 'Yuna', 'Yeji', 'Lia', 'Chaeryeong')


'''
    ลบข้อมูล
    del tuple_name -> ลบตัวแปรทิ้งพร้อมคืน Memory
'''
members3 = ("Yeji", "Yuna", "Lia")
print(members3) # ('Yeji', 'Yuna', 'Lia')
con_list = list(members3)
con_list.clear() # .remove(value) .clear()
members3 = tuple(con_list)
print(members3) # ()


'''
    ค้นหา เรียง นับจำนวน
'''
numbers1 = (23,5,6,23,906,22,567,2)
print(numbers1.index(5)) # 1
print(numbers1.count(23)) # 2
list_numbers1 = list(numbers1)
list_numbers1.sort()
numbers1 = tuple(list_numbers1)
print(numbers1) # (2, 5, 6, 22, 23, 23, 567, 906)
list_numbers1.reverse()
numbers1 = tuple(list_numbers1)
print(numbers1) # (906, 567, 23, 23, 22, 6, 5, 2)


'''
    Assign value from tuple into variable
'''
x = (1,2,3,4)
a,b,c,d = x
print(a) # 1
print(c) # 3


'''
    สลับค่าใน tuple
'''
tup3 = (1,2)
tup4 = (3,4)
tup3,tup4 = tup4,tup3
print(tup3) # (3, 4)
print(tup4) # (1, 2)


'''
    Convert tuple to string
'''
cutname = ("J", "e", "n", "n", "y")
print(cutname) # ('J', 'e', 'n', 'n', 'y')
joinname = "".join(cutname)
print(joinname) # Jenny -> type str


'''
    Reverse tuple
'''
user_id = (11,12,13,14,15)
re_userid = reversed(user_id)
re_userid = tuple(re_userid)
print(re_userid) # (15, 14, 13, 12, 11)
username = "lorem"
username = tuple(reversed(username))
print(username) # ('m', 'e', 'r', 'o', 'l')