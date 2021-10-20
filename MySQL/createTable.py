import pymysql

db = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='arit',
                             cursorclass=pymysql.cursors.DictCursor)
print(db)
cursor = db.cursor()

cursor.execute("SELECT VERSION()")
ver = cursor.fetchone()
print("Database version : %s " % ver)
db.close()