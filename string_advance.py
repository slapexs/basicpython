print("String index")
text = "lorem ipsum"
name = "  Rose  "

print(len(text)) # 11
print(text[0]) # l
print(text[0:3]) # lor
print(text[:4]) # lore
print(text[2:7]) # rem i
print(text[-1]) # m
print(text[-2]) # u
print(text[-3:]) # sum

print("-------------")
print("Trim space")
'''
    Trim space
    .strip() -> ตัดช่องว่างทั้ง 2 ข้าง
    .lstrip() -> ตัดช่องว่างด้านซ้าย
    .rstrip() -> ตัดช่องว่างด้านขวา
'''
print(name)
print(len(name))
print(name.strip())
print(len(name.strip()))

print("-------------")
print("String format")
'''
    String format
    name = "YUna"
    name.upper() -> YUNA
    name.lower() -> yuna
    name.capitalize() -> Yuna
'''
yuna = "YUna"
print(yuna.upper()) # YUNA
print(yuna.lower()) # yuna
print(yuna.capitalize()) # Yuna

print("-------------")
print("Replace string")
'''
    Replace string
    ryujin = "ruyjin"
    ryujin.replace("ruyjin", "ryujin") -> ryujin
'''

ryujin = "ruyjin"
print(ryujin.replace("ruyjin", "ryujin")) # ryujin
setnumber = "3-3-3-3"
print(setnumber.replace("3", "5", 1)) # 5-3-3-3
print(setnumber.replace("3", "5", 2)) # 5-5-3-3

print("-------------")
print("Check word in string")
'''
    Check word in string
'''
detail = "lorem ipsum"
str_in = "rem" in detail
str_notin = "ip" not in detail
print(str_in) # True
print(str_notin) # False


print("-------------")
print("String concatinate")
fname = "Lorem"
lname = "Ipsum"
age = "32"
print("Fname:" + fname + "\tLname:"+lname+"\tAge:"+age) # OG string concatinate

string_format = "Fname:{}\t Lname:{}\t Age:{}"
string_format1 = "Fname:{1}\t Lname:{0}\t Age:{2}"
print(string_format.format(fname, lname, age)) # Format string use it!!!
print(string_format1.format(fname, lname, age)) # Format string but with index

print("-------------")
print("Count word in string")
fruits = "ส้ม ส้ม ส้ม แอปเปิ้ล มะละกอ กล้วยส้ม"
print(fruits.count("ส้ม")) # 4

print("-------------")
print("Check start/end word")
word = "Amoung us"
print(word.startswith("ABC")) # False
print(word.endswith("us")) # True
