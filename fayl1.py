import sqlite3

# def createusertable():
#     database = sqlite3.connect('baza.sqlite')
#     cursor = database.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS users(
#     user_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
#     fullname VARCHAR,
#     username VARCHAR,
#     chatid INTEGER UNIQUE
#     )''')
#     database.commit()
#     database.close()
#
# createusertable()

def registruser(ism, faydalanuvchinomi, chat_id):
    database = sqlite3.connect('baza.sqlite')
    cursor = database.cursor()
    cursor.execute('''INSERT INTO users(fullname, username, chatid)
    VALUES(?,?,?)
    ''', (ism, faydalanuvchinomi, chat_id))

    database.commit()
    database.close()
