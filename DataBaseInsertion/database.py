import mysql.connector as mysql
from DataBaseInsertion import CreateDbEntry
from DataBaseInsertion import UpdateDbEntry
from SQLUsers import AddUser
import os
import TickerSearch

mydb = mysql.connect(host=os.getenv("SQL_HOST"), port="3306",
                     user=os.getenv("SQL_USER"), password=os.getenv("SQL_PASSWORD"),
                     database="stockmarketdata")

cursor = mydb.cursor()

num = input(
    "What do you want to do-\n1. Create a new Stock Database.\n2. Update a Stock Database.\nEnter your choice: ")

if num == '1':
    symbol = TickerSearch.get_symbol()
    CreateDbEntry.create_entry(symbol, cursor)

if num == "2":
    UpdateDbEntry.UpdateEntry(cursor)

if num =='3':
    AddUser.CreateUser(cursor)

# close the connection to the database.
mydb.commit()
cursor.close()
print("Done")
