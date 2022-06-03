'''
    File
        - Text file
        - Binary file

    Mode
        r = read
        w = write
        x = create new file
        t = text file
        b = binary file
        a = append

    โครงสร้าง
    * = require
    open(*file, *mode, encode)
'''


'''
    อ่านไฟล์
'''
fr = open("student.txt", "r", encoding="utf-8")
print(fr) # <_io.TextIOWrapper name='file/student.txt' mode='r' encoding='cp1252'>
print(fr.read()) # Student file นี่คือภาษาไทย
fr.close()

# with open("student.txt", "r", encoding="utf8") as file:
#     text = file.read()
#     print(text)


frl = open('score.txt', 'r', encoding='utf-8')
# line = frl.readline()
# print(line) # [["Yuna", 55], ["Yeji", 65]]This is example score
lines = frl.readlines()
for i in lines:
    print("->", i)
    '''
        -> [["Yuna", 55], ["Yeji", 65]]This is example score
        -> New line
    '''


'''
    สร้างไฟล์ใหม่ (เขียนทับทั้งหมด)
    variable = open(*file, "w", encoding)
    variable.write(data)
    variable.close()
'''
fw = open("score.txt", "w", encoding='utf-8')
fw.write("[[\"Yuna\", 55], [\"Yeji\", 65]]") # score.txt -> [["Yuna", 55], ["Yeji", 65]]
fw.writelines("This is example score\n")
fw.write("New line")
fw.close()


'''
    เพิ่มข้อมูลต่อท้าย
    x = open(*file, *"a", encoding)
'''
fadd = open("score.txt", "a", encoding='utf-8')
fadd.writelines("\nThis text from append mode")
for i in range(10):
    data = "\nscore:" + str(i)
    fadd.write(data)
fadd.close()


'''
    Delete file
    require
        - import os

    os.remove(*file)
'''

import os
try:
    if os.path.exists('fordel.txt'):
        os.remove('fordel.txt')
        print("Deleted")
    else:
        # print("File not found")
        raise Exception("Not found")
except Exception as e:
    print("Error->", e)