import sqlite3
con = sqlite3.connect('test.db')
con.execute('''DROP TABLE IF EXISTS product''')
print('Drop Table Successfully')