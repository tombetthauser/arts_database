import sqlite3

def connect():
  conn=sqlite3.connect("data.db")
  cur=conn.cursor()
  # cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
  conn.commit()
  conn.close()

def view():
  conn=connect.sqlite3("data.db")
  cur=conn.cursor()
  cur.execute("SELECT * FROM data")
  conn.close()

connect()