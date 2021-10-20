import sqlite3
con = sqlite3.connect('test.db')
con.execute('''UPDATE product SET prodName =
'Galaxy J7-11' WHERE prodID = 3''')
con.commit()
print('Update Successfully')