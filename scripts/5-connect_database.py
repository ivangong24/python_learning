# If you want to connect to a database, you need to install the pyodbc package.

import pyodbc

# Connect to the database
conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Database\xxx.accdb;'
    r'PWD=123456'
)

# show all table names

cursor = conn.cursor()
for table_info in cursor.tables(tableType='TABLE'):
    print(table_info.table_name)
cursor.close()

# create a data frame from a table

import pandas as pd

sql = 'SELECT * FROM tbl_xxx'

df = pd.read_sql(sql, conn)

print(df.head())

# close the connection

conn.close()
    
