import sqlite3
try:
    con = sqlite3.connect('test.db')
    con.execute('''INSERT INTO product (prodID,prodName,price)
    VALUES (1, 'Galaxy SIII',7000.00)''')

    con.execute('''INSERT INTO product (prodID,prodName,price)
        VALUES (2, 'iPad mimi',12000.00)''')

    con.execute('''INSERT INTO product (prodID,prodName,price)
        VALUES (3, 'Galaxy 5s',17000.00)''')

    con.execute('''INSERT INTO product (prodID,prodName,price)
        VALUES (4, 'Galaxy NoteII',13000.00)''')

    con.execute('''INSERT INTO product (prodID,prodName,price)
        VALUES (5, 'Galaxy Note8',14000.00)''')
    con.commit()
    print("Record Successfully")
except con.Error as e:
    if con:
        con.rollback()
        print("Error %s:" % e.args[0])
finally:
    if con:
        con.close()