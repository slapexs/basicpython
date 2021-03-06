'''
    Module
    import other program from other file for use in main file

    โครงสร้าง
    import file_module_name

    variable = file_module_name.function_name(parameter)
'''

import calculate
import cats

result_addition = calculate.addition(10,20,30,40,50,60)
print(result_addition) # 210
print(calculate.subtraction(10,2)) # 8
print(cats.getfact())


'''
    Set alias name for module
    โครงสร้าง
    import module_name as alias_name

    import thisismodaulenamesolong as mymodule
'''


'''
    From module
    เลือกฟังก์ชันบางตัวจาก module มาเพื่อใช้งาน
    โครงสร้าง
    from module_name import some_function
'''
from cats import geturlcatfact

print(geturlcatfact(2))


'''
    Import all function from module
    โครงสร้าง
    from module_name import *
'''