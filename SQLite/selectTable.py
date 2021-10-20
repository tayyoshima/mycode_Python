import sqlite3
print("ProductID       ProductName        Price")
print("--------------------------------------------")
con = sqlite3.connect('test.db')
data = con.execute('''SELECT * FROM product''')
print(data)
for row in data:
    print('   ',row[0],'         ',row[1],'      ',row[2])