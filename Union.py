import csv

names_tables=["GDP","human-development-index","Inflation","life-expactancy","population","Unemploymend","WDI"]

#Country Name, country code, value, year
def merge_csv(file1, output_file):
    table = []


    with open(r'C:\Users\User\Desktop\Домашка\ВКР\DataBase\Python\DBTRUE\{}.csv'.format(file1[0]),
              'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            table.append([row[0],row[1],row[3],row[2]])

    for some_file in file1[1:7]:
        table_second = []
        df = []
        #i=[country,code,year,value]
        with open(r'C:\Users\User\Desktop\Домашка\ВКР\DataBase\Python\DBTRUE\{}.csv'.format(some_file), 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            for row in reader:
                table_second.append([row[0], row[1], row[3], row[2]])



        for i in table:
            mayachok=False
            for j in table_second:
                if i[1]==j[1] and i[2]==j[2]:
                    df.append(i+[j[3]])
                    mayachok=True

            if mayachok == False:
                df.append(i+["0"])


        table=df



    with open(f'{output_file}', 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        for i in table:
            writer.writerow(i)

# Вызов функции merge_csv с вашими именами файлов
merge_csv(names_tables, 'new.csv')
