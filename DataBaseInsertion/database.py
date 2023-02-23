import mysql.connector as mysql
from DataBaseInsertion import CreateDbEntry
import os
import TickerSearch

mydb = mysql.connect(host='localhost', port="3306", user=os.getenv("SQL_USER"), password=os.getenv("SQL_PASSWORD"),
                     database="stockmarketdata")

cursor = mydb.cursor()

num = input(
    "What do you want to do-\n1. Create a new Stock Database.\n2. Update a Stock Database.\nEnter your choice: ")

if num == '1':
    symbol = TickerSearch.get_symbol()
    CreateDbEntry.create_entry(symbol, cursor)

if num == "2":
    cursor.execute("SHOW TABLES")
    cmp_list = []
    myresult = cursor.fetchall()
    for res in myresult:
        res = str(res)
        cmp_list.append(res[2:-3])

    print("Available Companies In Database are:", cmp_list)
    j = input("Type the name of any one: ")
    cursor.execute("DROP TABLE stockmarketdata." + j + ";")
    j = j.replace("_", ".")
    CreateDbEntry.create_entry(j, cursor)

# close the connection to the database.
mydb.commit()
cursor.close()
print("Done")
