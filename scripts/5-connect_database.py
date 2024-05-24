# If you want to connect to a database, you need to install the pyodbc package.

import pyodbc

# Connect to the database
conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Database\xxx.accdb;'
    r'PWD=123456'
)

cursor = conn.cursor()
cursor.execute('select * from tbl_xxx')
for row in cursor.fetchall():
    print (row)
    
