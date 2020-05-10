import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()

# exist = False
# for i in cur.execute("""SELECT id FROM Table1""").fetchall():
# if 1234543 == i:
# exist = True
# if not exist:
# cur.execute("""INSERT INTO Table1(id) VALUES(12345432)""")
# con.commit()

# cur.execute("""DELETE FROM Table1""")
# result = cur.execute("""SELECT id FROM Table1""").fetchall()
# print(result)
# con.commit()


def new_user(user_id):
    exist = False
    for i in cur.execute("""SELECT id FROM Table1""").fetchall()[0]:
        if user_id == i:
            exist = True
            break
    if not exist:
        cur.execute(f"INSERT INTO Table1(id) VALUES({user_id})")
        con.commit()
