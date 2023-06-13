import csv
name_table=[]
table=[]
new=[]
finish_table=[]

def reader():
    with open(r'C:\Users\User\Desktop\Домашка\ВКР\DataBase\Python\DataBases\population.csv',
              'r', newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        a=0
        for row in reader:
            table.append(row)

def new_reader():
    with open(r'C:\Users\User\Desktop\Домашка\ВКР\DataBase\Python\DataBases\HDI.csv',
              'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        a = 0
        for row in reader:
            table.append(row)

            if a == 0:
                name_table.append(row[0])
                name_table.append(row[1])
                name_table.append(row[2])
                name_table.append(row[3])
                name_table.append("HDI")
                name_table.append("Year")
            a += 1

def foring(file):
    try_one=0
    for i in file:
        abc = i
        if try_one != 0:
            abc.pop(-1)
            new.append(abc)
        else:
            new.append(abc)
        try_one+=1

def writer_file(file):
    with open(r'C:\Users\User\Desktop\Домашка\ВКР\DataBase\Python\DBTRUE\HDI.csv',
              'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        for i in file:
            writer.writerow(i)

def new_table(file):
    finish_table.append(name_table)
    year=""
    list_numbers=[a for a in range(len(file[0]))][5:len(file[0])]
    a=0
    for j in list_numbers:
        try_one = 0
        for i in file:
            number = 0
            print(i)
            print(a,try_one)
            if try_one==0:
                year=i[j]

            elif try_one!=0:
                number=i[j]

                if i[j]=="" or i[j]==" " or i[j]=="." or i[j]=="..":
                    number=0

                finish_table.append([i[0],i[1],i[2],i[3],number,year])
            try_one+=1
            a+=1

def getting_table():
    new_reader()
    # print(name_table)
    # print(len(table[105]))
    new_table(table)
    writer_file(finish_table)


def fix_table():
    reader()
    foring(table)
    writer_file(new)


getting_table()
