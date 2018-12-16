import sqlite3

# We connect to our Sqlite database, then we create a cursor
try:
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()

except ConnectionError:
    print("error to connect to the database")
