import mysql.connector as mysql
import pandas as pd

df = pd.read_csv("C:\\Users\\Admin\\Desktop\\JayMP\\daily_adjusted_IBM.csv",index_col="timestamp")

mydb = mysql.connect(host='stockmarketdatabase.ceiyghg6qepy.ap-south-1.rds.amazonaws.com', port="3306", user= "admin", password= "jAy7506003943",database="stockmarketdata")
cursor = mydb.cursor()


cursor.execute("CREATE TABLE `stockmarketdata`.`jaytest` (`date` TIMESTAMP NOT NULL,`open` DOUBLE "
                                                                     "NULL,`high` DOUBLE NULL,`low` DOUBLE NULL,"
                                                                     "`close` DOUBLE NULL,`adjusted close` DOUBLE "
                                                                     "NULL,`volume` DOUBLE NULL, `dividend amount` "
                                                                     "DOUBLE NULL,`split coefficient` DOUBLE NULL,"
                                                                     "PRIMARY KEY (`date`));")
                                                                     
x = df.to_records()
for i in range(len(df)):
    row = x[i].tolist()
    cursor.execute('INSERT INTO stockmarketdata.jaytest VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                           row)
print("done")
mydb.commit()
cursor.close()
        