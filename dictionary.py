'''
    Dictionary -> key, value
    โครงสร้าง -> {key:value, key:value}
        Normal ->  dictname = {"name": "Yuna", "age": 20}
        Constructor -> dictname = dict({name="Ryujin", age=21})
'''
person = {"name":"Yuna", "age":20, "position":"Singer", 2003:"born"}
print(person) # {'name': 'Yuna', 'age': 20, 'position': 'Singer'}
print(person["name"]) # Yuna
print(person[2003]) # born
print(person.get("age")) # 20


'''
    Edit value
    dictname[key] = new value
'''
person["name"] = "Yeji"
print(person["name"]) # Yeji


'''
    Add value
    ถ้า key ซ้ำจะเป็นการแก้ไขถ้าไม่ซ้ำจะเป็นการเพิ่มข้อมูลใหม่
    dictname.update({key:value, key:value})
'''
person.update({"BloodType": "A", "position": "Leader"})
print(person) # {'name': 'Yeji', 'age': 20, 'position': 'Leader', 2003: 'born', 'BloodType': 'A'}


'''
    Lopp for display
    Display key only
        for item in dict:
            print(item)
        
        for item in dict.keys():
            print(item)
    
    Display value only
        for item in dict.values():
            print(item)
    
    Display both
        for key, value in dict,items():
            print("key", key)
            print("value", value)
'''

for item in person.values():
    print(item)

for k, v in person.items():
    print("key:", k, "- value:", v)


'''
    ลบสมาชิก
    dict.pop(key) -> Delete value by key
    dict.popitem() -> Delete last value
    dict.clear() -> Delete all value
    del dict -> Delete dictionary variable
'''
print(person) # {'name': 'Yeji', 'age': 20, 'position': 'Leader', 2003: 'born', 'BloodType': 'A'}
person.pop(2003)
print(person) # {'name': 'Yeji', 'age': 20, 'position': 'Leader', 'BloodType': 'A'}
person.popitem()
print(person) # {'name': 'Yeji', 'age': 20, 'position': 'Leader'}
person.clear()
print(person) # {}
del person


'''
    Copy dictionary
    setB = setA.copy()
'''
a = {"name":"Jan"}
b = a.copy()
print(b) # {'name': 'Jan'}


'''
    dictionary in dictionary
    dict = {
        key1: {key: value},
        key2: {key: value}
    }
'''

class1 = {
    "room1": {"amount": 20},
    "room2": {"amount": 23}
}
print(class1) # {'room1': {'amount': 20}, 'room2': {'amount': 23}}
print(class1["room1"]) # {'amount': 20}
print(class1["room1"]["amount"]) # 20