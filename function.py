'''
    Function
    โครงสร้าง
        def function_name():
            statement
    เรียกใช้
        function_name()
'''

from audioop import findmax


def sayhi():
    print("Hello world")

sayhi()


'''
    Global variable / Local variable
'''

msg = "Msg without function" # Global variable
def display_msg():
    msg = "This is msg" # Local variable
    print("msg:", msg)

display_msg() # msg: This is msg -> from local variable
print(msg) # Msg without function -> from global variable


'''
    Pass parameter to function
    โครงสร้าง
        def function_name(param1, param2):
            print(param1)
        
        function_name(value1, value2)
        function_name(value1) -> Error
'''
def saymsg(msg):
    print("This is msg from param ->", msg)

saymsg("Yuna") # This is msg from param -> Yuna


'''
    Arguments / Parameter
    fname = "Dany" -> Arguments
    lname = "Stand" -> Arguments

    def showname(firstname, lastname): -> firstname, lastname -> Parameter
        statement
'''
fname  = "Dany"
lname = "Stand"
def showname(firstname, lastname):
    print("Firstname:", firstname, " Lastname:", lastname)

showname(fname, lname) # Firstname: Dany  Lastname: Stand


'''
    Arbitrary arguments aka *parameter_name
    เป็นฟังก์ชันที่สามารถส่ง argument ได้ไม่จำกัด
    
    โครงสร้าง
        def function_name(*some_name): -> ใช้ชื่ออะไรก็ได้แต่ต้อมี * อยู่หน้าชื่อ
            statement
'''
def shownumber(*numbers):
    print(numbers)
shownumber(1,2,3,4,5,6) # (1, 2, 3, 4, 5, 6)

def calnumber(*numbers):
    sum = 0
    for i in numbers:
        sum+=i
    print(sum)
calnumber(1,2,3,4,5,6) # 21


'''
    Keyword arguments
    โครงสร้าง
        def function_name(param1, param2, param3):
            statement

    เรียกใช้
        function_name(param1=value, param2=value, param3=value)
'''
def showdata(name, age, no):
    print("name:", name, "age:", age, "no:", no)

showdata(age=20, name="John", no=3) # name: John age: 20 no: 3


'''
    Default parameter
    โครงสร้าง
        def function_name(param1, param2="Bangkok"):
            statement
    เรียกใช้
        function_name(value1)
'''
def showprovice(name, province="Bangkok"):
    print("name:", name, "Province:", province)
showprovice("John") # name: John Province: Bangkok


'''
    List, Tuple, Set, Dict parameter
    โครงสร้าง
        def function_name(Non primitive data):
            statement
    เรียกใช้
        function_name(Non primitive data)
'''
fruits = ["Mango", "apple"]
def displaylist(list):
    print(list)
displaylist(fruits) # ['Mango', 'apple']


'''
    Return function
    โครงสร้าง
        def function_name(param):
            return statement
    เรียกใช้
        variable = function_name(param)
'''
def calab(a, b):
    return a+b
result = calab(30,28)
print(result) # 58


def checkage(age):
    if age < 18:
        return # -> End function
    else:
        return "Age" + str(age)

resultage = checkage(19)
print(resultage) # Age19
print(checkage(17)) # None


'''
    Arbitrary arguments aka **kwargs
    โครงสร้าง
        def function_name(**kwagrs): -> ใช้ชื่ออะไรก็ได้แต่ต้องมี ** อยู่หน้าตัวแปร
            statement
    เรียกใช้
'''

def displaydata(**items):
    print(items)
displaydata(fname="Ye ji", lname="Hwang", age=22) # {'fname': 'Ye ji', 'lname': 'Hwang', 'age': 22}


'''
    Call function in function
'''
def findMax(x, y):
    return x if x>y else y
print(findMax(10,20)) # 20

def compare(x, y, z):
    a = findMax(x, y)
    b = findMax(a, z)
    return b
print(compare(1,2,3)) # 3


'''
    Recursive function -> ฟังก์ชันที่เรียกใช้ตัวเอง
'''

def printnumber(number):
    print(number)
    number+=1
    if number <= 10:
        printnumber(number)
    
printnumber(0) # -> 0 - 10

def factorial(number):
    if number == 1:
        return number
    else:
        return number*factorial(number-1)
print(factorial(5)) # 15

def fibonacci(number):
    return number if number <= 1 else fibonacci(number-2)+fibonacci(number-1)
    '''
        if number <= 1:
            return number
        else:
            return fibonacci(number-2)+fibonacci(number-1)
    '''
for i in range(10):
    print(fibonacci(i)) # 0,1,1,2,3,4,8,13,21,34


'''
    Pass in function
'''

def getname():
    pass
getname() # 

'''
    Lambda function
    โครงสร้าง
        lambda arguments: expression
    เรียกใช้
        x = x(arguments)
'''

hername = lambda msg: msg
print(hername("Yuna")) # Yuna

plusnumber = lambda x,y: y+x
print(plusnumber(5,10)) # 15
