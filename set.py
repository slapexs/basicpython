'''
    Set
    - ไม่สามารถแก้ไขข้อมูลได้
    - ไม่สามารถใส่ข้อมูลซ้ำกันได้
    - ไม่มีเลขลำดับ Index
    - แสดงผลไม่เรียงลำดับ

    สร้างแบบปกติ -> setname{}
    สร้างแบบ Contructor -> setname = set(["Hi~", 12, 3.14, True])
'''
fish = {"Salmon", "Tuna", "catfish"}
# fish1 = {"Salmon", "Tuna", "catfish", "Salmon"} -> Error
# Constructor
same_fish = set(["Salmon", "Tuna", "catfish"])

'''
    เพิ่มข้อมูลสมาชิก
    1 ค่า
        setname.add(value)

    มากกว่า 1 ค่า
        setname.update(list) or setname.update([value1, value2, value3])

'''
print(fish) # {'catfish', 'Salmon', 'Tuna'}
fish.add("Puffer fish")
print(fish) # {'Puffer fish', 'catfish', 'Salmon', 'Tuna'}
more_fish = ["Eel", "Guppy"]
fish.update(more_fish)
print(fish) # {'catfish', 'Guppy', 'Eel', 'Salmon', 'Puffer fish', 'Tuna'}


'''
    นับจำนวนสมาชิก
    len(setname)
'''
print(len(fish)) # 6


'''
    ลบสมาชิก
    setname.remove(value) -> ถ้า value นั้นไม่มีใน set จะ Error
    setname.discard(value) -> ถ้าเจอ value จะลบถ้าไม่เจอจะข้ามไป
    setname.clear() -> ลบค่าใน set ออกเหลือแค่ set ว่าง
    del setname -> ลบตัวแปร
'''
print(fish) # {'Puffer fish', 'Eel', 'Salmon', 'catfish', 'Guppy', 'Tuna'}
fish.remove("Eel")
print(fish) # {'Puffer fish', 'Salmon', 'catfish', 'Guppy', 'Tuna'}
fish.discard("Organic fish")
print(fish) # {'Tuna', 'Salmon', 'Guppy', 'catfish', 'Puffer fish'}
fish.clear()
print(fish) # set()