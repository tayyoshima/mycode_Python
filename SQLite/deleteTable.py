import sqlite3
con = sqlite3.connect('test.db')
con.execute('''DELETE from product WHERE prodID = 2''')
con.commit()
print('Delete Successfully')