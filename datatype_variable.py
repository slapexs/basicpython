# ชนิดข้อมูล
'''
    Datatype

    [Primitive]
        Integer -> int -> เลขจำนวนเต็ม เช่น 1, 2, 3, 50, 459,220
        Floating point -> float -> เลขทศนิยม เช่น 1.0 3.99
        String -> str -> ตัวหนังสือ
        Booleans -> bool -> True, False
        
    [Non primitive]
        List -> list -> object (like a array) เช่น [1, "Rose", 3.99, True]
        Dictionaties -> dict -> ชุดข้อมูลไม่มีลำดับ {"name": "Tony", "age": 39}
        Tuples -> tup -> ชุดข้อมูล (10, "Hello", 200.3)
        Sets -> set -> ชุดข้อมูลไม่เรียงลำดับ ("a","b")

    Variable
    variable_name = value
'''

x = 23
y = "Monday"
z = True

print(x)
print(y + str(x)) # แปลง x ให้เป็น String เพื่อให้ต่อข้อความได้
# output Monday23

'''
    type(variable)
    ใช้แสดง datatype ของตัวแปร
'''
int_type = type(x)
print(int_type)
