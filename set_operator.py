# ตัวดำเนินการของ Set ทางคณิตศาสตร์

'''
    Union -> รวมกันทั้งหมด
    setA.update(setB)
'''
fruit_a = {"Mango", "Apple", "Star fruit"}
fruit_b = {"Mangosteen", "Watermelon", "Coconut"}
fruit_a.update(fruit_b)
print(fruit_a) # {'Mango', 'Star fruit', 'Watermelon', 'Mangosteen', 'Apple', 'Coconut'}


'''
    Copy set
'''
fruit_c = fruit_a.copy()
print(fruit_c) # {'Apple', 'Star fruit', 'Mango', 'Coconut', 'Watermelon', 'Mangosteen'}


'''
    Difference -> เป็นการถามว่าใน setA ข้อมูลไหนบ้างที่ไม่มีใน setB
    diff_set = setA.difference(setB)
'''
diff_fruit  = fruit_a.difference(fruit_b)
print(diff_fruit) # {'Mango', 'Star fruit', 'Apple'}


'''
    Intersection -> สมาชิกตัวไหนบ้างที่มีทั้ง 2 sets
    intersection_set = setA.intersection(setB)
    setA.differance_update(setB) -> นำสมาชิกใน setA ที่ไม่มีใน setB มาใส่ค่าใหม่ใน setA
    setA.intersection_update(setB) -> นำสมาชิกใน setA ที่มีใน setB มาใส่ค่าใหม่ใน setA
'''
number_a = {1,2,3,4,5}
number_b = {4,5,6,7,8}
number_c = {1,2,3}
number_d = {2,3,4}
inter_number = number_a.intersection(number_b)
print(inter_number) # {4, 5}
diff_number = number_a.difference(number_b)
print(diff_number) # {1, 2, 3}
number_a.difference_update(number_b)
print(number_a)  # {1, 2, 3}
number_c.intersection_update(number_d)
print(number_c) # {2, 3}


'''
    Subset
    setB.issubset(setA) -> ข้อมูลทั้งหมดใน setB มีอยู่ใน setA มั้ย
    setA.issuperset(setB) -> ข้อมูลบางตัวใน setA มีอยู่ใน setB มั้ย
'''
pets = {"Dog", "Cat", "Rabbit", "Bird", "Fish"}
exo_pets1 = {"Snake", "Bat", "Bird"}
exo_pets2 = {"Cat", "Bird"}
print(exo_pets1.issubset(pets)) # False
print(exo_pets2.issubset(pets)) # True
print(pets.issuperset(exo_pets2)) # True


'''
    Min, Max of set
    min(setname)
    max(setname)
'''
number_e = {1,2,3,4,5}
print(min(number_e)) # 1
print(max(number_e)) # 5


'''
    Frozen set
'''
roles = frozenset(["admin", "staff", "student"])
print(roles) # frozenset({'staff', 'admin', 'student'})
# roles.add("user") -> Error
# roles.remove("admin") -> Error