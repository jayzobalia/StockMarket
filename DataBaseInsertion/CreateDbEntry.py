import StockDataframe
import pandas as pd
import os


def create_entry(symbol, cursor):
    StockDataframe.get_df(symbol, "full")
    symbol = symbol.replace(".", "_")
    csv_data = pd.read_csv("DataBaseInsertion\\Stock CSVs\\xx.csv", index_col="date")
    os.remove("DataBaseInsertion\\Stock CSVs\\xx.csv")

    try:
        cursor.execute("CREATE TABLE `stockmarketdata`.`" + symbol + "` (`date` TIMESTAMP NOT NULL,`open` DOUBLE "
                                                                     "NULL,`high` DOUBLE NULL,`low` DOUBLE NULL,"
                                                                     "`close` DOUBLE NULL,`adjusted close` DOUBLE "
                                                                     "NULL,`volume` DOUBLE NULL, `dividend amount` "
                                                                     "DOUBLE NULL,`split coefficient` DOUBLE NULL,"
                                                                     "PRIMARY KEY (`date`));")
        x = csv_data.to_records()
        for i in range(len(csv_data)):
            row = x[i].tolist()
            cursor.execute('INSERT INTO stockmarketdata.' + symbol + ' VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                           row)
    except:
        print("Database Of This Company Already Exists")
