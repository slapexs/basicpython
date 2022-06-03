import os

# file_add = open("list_users.txt", 'a', encoding='utf-8')
# for i in range(10):
#     template_data = "ID:{},score:{}\n"
#     file_add.write(template_data.format(i, "user"+str(i+1000)))
# file_add.close()

def showdata(file):
    rawdata = open(file, 'r', encoding='utf-8')
    datastring = rawdata.readlines()
    # print(datastring)
    listdata = []
    # print(datastring[0])
    
    for i in range(len(datastring)):
        cutstr = datastring[0].split(",")
        cutstr_id = cutstr[0].split(':')
        cutstr_username = cutstr[1].split(':')
        datai = {"id":cutstr_id[1], "username":cutstr_username[1]}
        listdata.append(datai)
    print(listdata)


showdata("list_users.txt")