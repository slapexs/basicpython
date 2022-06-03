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

# with open("student.txt", "r", encoding="utf8") as file:
#     text = file.read()
#     print(text)
