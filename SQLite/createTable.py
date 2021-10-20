import sqlite3
try:
    con = sqlite3.connect("test.db")
    con.execute('''CREATE TABLE product
    (prodID INT PRIMARY KEY NOT NULL, 
    prodName TEXT,price REAL);''')
    print('Table created Successfully')
except con.Error as e:
    print('Error %s: ' % e.args[0])
con.close()