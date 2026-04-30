import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('caleb_kitchens.db')
        return con
    except Error as e:
        print(e)

def sql_table(con):
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Music_Artists(artist text PRIMARY KEY, genre text NOT NULL, number_recordings integer NOT NULL)")
    con.commit()

def sql_insert(con, artists):
    cursor = con.cursor()
    cursor.executemany('INSERT OR IGNORE INTO Music_Artists VALUES (?,?,?)', artists)
    con.commit()

def sql_fetch(con):
    cursor = con.cursor()
    cursor.execute('SELECT * FROM Music_Artists')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def sql_fetch_rock(con):
    cursor = con.cursor()
    cursor.execute('SELECT * FROM Music_Artists WHERE genre = "Rock"')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

artists_to_insert = [("Miley", "Rock", 14), ("Dolly", "Country", 123), ("Eminem", "HipHop", 98), ("Brittany", "Rock", 37)]

con = sql_connection()

sql_table(con)
sql_insert(con, artists_to_insert)
sql_fetch(con)
print("\n")
sql_fetch_rock(con)

