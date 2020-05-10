import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()


def new_user(user_id):
    exist = False
    for i in cur.execute("""SELECT id FROM Table1""").fetchall()[0]:
        if user_id == i:
            exist = True
            break
    if not exist:
        cur.execute(f"INSERT INTO Table1(id) VALUES({user_id})")
        cur.execute("""INSERT INTO Table1(reminder_creation) VALUES(0)""")
        con.commit()


def reminder_creation(user_id):
    if cur.execute("""SELECT reminder_creation FROM Table1 WHERE id = ?""", (user_id,)).fetchall()[0][0] == 1:
        return True
    else:
        return False


def reminder_creation_change(user_id):
    if cur.execute("""SELECT reminder_creation FROM Table1 WHERE id = ?""", (user_id,)).fetchall()[0][0] == 1:
        cur.execute("""UPDATE Table1 SET reminder_creation = 0 WHERE id = ?""", (user_id,))
    else:
        cur.execute("""UPDATE Table1 SET reminder_creation = 1 WHERE id = ?""", (user_id,))
    con.commit()
    # print(cur.execute("""SELECT reminder_creation FROM Table1 WHERE id = ?""", (user_id,)).fetchall()[0][0])


def reminder_datetime_save(user_id, datetime):
    cur.execute("""UPDATE Table1 SET reminder_datetime = ? WHERE id = ?""", (datetime, user_id,))
    con.commit()


def reminder_text_save(user_id, text):
    cur.execute("""UPDATE Table1 SET reminder_text = ? WHERE id = ?""", (text, user_id,))
    con.commit()


def reminder_delete(user_id):
    cur.execute("""UPDATE Table1 SET reminder_datetime = ? WHERE id = ?""", ("", user_id,))
    cur.execute("""UPDATE Table1 SET reminder_text = ? WHERE id = ?""", ("", user_id,))
    con.commit()


def reminder_print(user_id):
    return cur.execute("""SELECT reminder_datetime FROM Table1 WHERE id = ?""", (user_id,)).fetchall()[0][0], \
           cur.execute("""SELECT reminder_text FROM Table1 WHERE id = ?""", (user_id,)).fetchall()[0][0]


def reminder_exist(user_id):
    if cur.execute("""SELECT reminder_datetime FROM Table1 WHERE id = ?""", (user_id,)).fetchall()[0][0] != "":
        return True
    else:
        return False
