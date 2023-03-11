import mysql.connector
import os

# Connect to MySQL server
mydb = mysql.connector.connect(host="localhost", port="3306",
                               user="jayzobalia", password="J@y447506003943",
                               database="stockmarketdata")

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Execute SQL query to create user
mycursor.execute("CREATE USER 'xyzz'@'localhost' IDENTIFIED BY 'jaylovesprisha'")

# Grant necessary privileges to the user
mycursor.execute("GRANT SELECT, INSERT ON stockmarketdata.* TO 'xyzz'@'localhost'")

# Commit changes to the database
mydb.commit()

# Close the database connection
mydb.close()
