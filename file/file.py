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
from base64 import encode


fr = open("student.txt", "r", encoding="utf-8")
print(fr) # <_io.TextIOWrapper name='file/student.txt' mode='r' encoding='cp1252'>
print(fr.read()) # Student file นี่คือภาษาไทย

# with open("student.txt", "r", encoding="utf8") as file:
#     text = file.read()
#     print(text)


'''
    สร้างไฟล์ใหม่
    variable = open(*file, "r", encoding)
    variable.write(data)
    variable.close()
'''
fw = open("score.txt", "w", encoding='utf-8')
fw.write("[[\"Yuna\", 55], [\"Yeji\", 65]]") # score.txt -> [["Yuna", 55], ["Yeji", 65]]
fw.writelines("This is example score\n")
fw.write("New line")
fw.close()
