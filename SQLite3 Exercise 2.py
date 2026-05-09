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
    cursor.execute('CREATE TABLE IF NOT EXISTS Music_Artists(artist text PRIMARY KEY, genre text NOT NULL, number_recordings integer NOT NULL)')
    cursor.execute('CREATE TABLE IF NOT EXISTS Genres(genre text PRIMARY KEY, city text NOT NULL)')
    cursor.execute('CREATE TABLE IF NOT EXISTS Cities(city text PRIMARY KEY, state text NOT NULL, zip_code integer NOT NULL, population integer NOT NULL)')
    con.commit()

def sql_insert(con, artists, genres, cities):
    cursor = con.cursor()
    cursor.executemany('INSERT OR IGNORE INTO Music_Artists VALUES (?,?,?)', artists)
    cursor.executemany('INSERT OR IGNORE INTO Genres VALUES (?,?)', genres)
    cursor.executemany('INSERT OR IGNORE INTO Cities VALUES (?,?,?,?)', cities)
    con.commit()

def sql_fetch(con):
    cursor = con.cursor()

    cursor.execute('SELECT * FROM Music_Artists')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    print("\n")

    cursor.execute('SELECT * FROM Genres')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    print("\n")

    cursor.execute('SELECT * FROM Cities')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def sql_fetch_match(con):
    cursor = con.cursor()

    cursor.execute('SELECT * FROM Music_Artists INNER JOIN Genres ON Music_Artists.genre = Genres.genre')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def sql_fetch_artist_details(con, artist):
    cursor = con.cursor()

    query = '''SELECT  
                Genres.genre,
                Music_Artists.artist,
                Music_Artists.number_recordings,
                Cities.city,
                Cities.population
            FROM Music_Artists 
            LEFT JOIN Genres
                ON Music_Artists.genre = Genres.genre
            LEFT JOIN Cities
                ON Genres.city = Cities.city
            WHERE artist = ?'''

    cursor.execute(query, (artist,))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            if row[3]:
                city = f"most popular in {row[3]} with a population of {row[4]}"
            else:
                city = "popular everywhere"
            print(f"\n{row[0]} artist {row[1]} has {row[2]} recordings and is {city}.")






artists_to_insert = [("Miley", "Rock", 14), ("Dolly", "Country", 123), ("Eminem", "HipHop", 98), ("Brittany", "Rock", 37)]
genres_to_insert = [("Rock", "Los Angeles"), ("Hippie", "Eugene"), ("Opera", "Florence")]
cities_to_insert = [("Los Angeles", "CA", 66666, 10000000), ("Eugene", "OR", 55555, 80000), ("Nashville", "TN", 11111, 1500000)]

database_con = sql_connection()

sql_table(database_con)
sql_insert(database_con, artists_to_insert, genres_to_insert, cities_to_insert)
sql_fetch(database_con)
print("\n")
sql_fetch_match(database_con)
print("\n")

artist = input("Which artist would you like to know about? ")
sql_fetch_artist_details(database_con, artist)

