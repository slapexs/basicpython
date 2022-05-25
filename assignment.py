'''
    การเรียงข้อมูล
    .sort() -> น้อยไปมาก
    .reverse() -> ย้อนกลับ
    list = list[::-1] -> เรียงลำดับใหม่จากหลังมาหน้าใน List เดิม
'''

numbers = [23,1,5,76,82,7,90,23,2,44,57]
print(numbers) # [23,1,5,76,82,7,90,23,2,44,57]
numbers.sort()
print(numbers) # [1, 2, 5, 7, 23, 23, 44, 57, 76, 82, 90]
numbers.reverse()
print(numbers) # [90, 82, 76, 57, 44, 23, 23, 7, 5, 2, 1]
numbers = numbers[::-1]
print(numbers) # [1, 2, 5, 7, 23, 23, 44, 57, 76, 82, 90]

'''
    หาค่ามากสุด น้อยสุด
    min(list)
    max(list)
'''
print(numbers) # [23,1,5,76,82,7,90,23,2,44,57]
print(min(numbers)) # 1
print(max(numbers)) # 90


'''
    ผลรวม
    sum(list)
'''
print(numbers) # [23,1,5,76,82,7,90,23,2,44,57]
print(sum(numbers)) # 410


'''
    จับคู่คข้อมูลจาก 2 List
    for x,y,z in zip(list1, list2, list3):
        statement
'''
fruits = ["Apple", "Banana", "Mango"]
prices = [10,20,30]
weight = [1,2,3]

for x,y,z in zip(fruits, prices, weight):
    print(x,"->",y, "->", z)


'''
    นับจำนวนตัวอักษร
    .count(value)
'''
msg = ["aa", "ab", "abc", "aabc"]
print(msg[0].count("a")) # 2
