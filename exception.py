'''
    Exception
    สำหรับจัดการกับ Error ที่ไม่ได้ตั้งใจ

    โครงสร้าง
    try:
        statement success
    except:
        statement error
'''

def shownumber(number):
    try:
        print(number/2)
    except:
        print("Exception")

shownumber("Hi") # Exception


'''
    Exception หลายเหตุการณ์
    โครงสร้าง
    try:
        statement success
    except Errorname:
        statement error
'''

try:
    number1 = 10
    act1 = number1/"a" # Errorname -> ZeroDivisionError
except TypeError:
    print("TypeError") # 10/"a" -> TypeError
except ZeroDivisionError:
    print("ZeroDivisionError") # 10/0 -> ZeroDivisionError
except ValueError:
    pass


'''
    ลดรูป Exception
    โครงสร้าง
    try:
        statement success
    except Exception as e:
        statement error
'''

try:
    number2 = 20
    sum = number2/0
    print(sum)
except Exception as e:
    print(e)
    '''
        10/"a" -> unsupported operand type(s) for /: 'int' and 'str'
        10/0 -> division by zero
    '''


'''
    Else in Exception
    โครงสร้าง
    try:
        statement success
    except Exception as e:
        statement error
    else:
        statement
'''

try:
    sum2 = 22/1
except Exception as e:
    print(e)
else:
    print("Program finish")
    '''
        22/0 -> division by zero
        22/1 -> Program finish
    '''


'''
    Finally in Exception
    ไม่ว่าจะ Error หรือไม่ก็จำทำงานใน finally
    โครงสร้าง
    try:
        statement success
    except:
        statement error
    finally:
        statement
'''
try:
    sum3 = 22/0
except Exception as e:
    print(e)
    print("123333")
finally:
    print("Finally statement")
    '''
        output
        division by zero
        Finally statement
    '''


'''
    Exception with Raise
    โครงสร้าง
    try:
        statement success
        if manual error:
            raise Exception("message")
    except Exception as e:
        statement error
'''

try:
    num1 = -1
    if num1<0:
        raise Exception("num1 < 0")
    else:
        print(num1)
except Exception as e:
    print("Error detected: ", e) # Error detected:  num1 < 0