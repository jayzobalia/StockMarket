import CreateDbEntry

def UpdateEntry(cursor):
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