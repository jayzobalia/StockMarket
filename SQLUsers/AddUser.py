def CreateUser(cursor):
    username = input("Enter your Username: ")
    password = input("Enter your Password: ")

    cursor.execute("CREATE USER '" + username + "'@'localhost' IDENTIFIED BY '" + password + "'")
    cursor.execute("GRANT SELECT, INSERT ON stockmarketdata.* TO '" + username + "'@'localhost'")