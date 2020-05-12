import sqlite3

# def connect():
#   conn=sqlite3.connect('data.db')
#   cur=conn.cursor()
#   # cur.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)')
#   conn.commit()
#   conn.close()

def all_rows():
  conn=sqlite3.connect('data.db')
  cur=conn.cursor()
  cur.execute('SELECT * FROM data;')
  rows=cur.fetchall()
  conn.close()
  return rows

def total_count():
  conn=sqlite3.connect('data.db')
  cur=conn.cursor()
  cur.execute('SELECT COUNT(*) FROM data;')
  rows=cur.fetchall()
  conn.close()
  return rows

def user_query(query):
  query = enforce_semicolon(query)
  conn=sqlite3.connect('data.db')
  cur=conn.cursor()
  cur.execute(query)
  rows=cur.fetchall()
  conn.close()
  return rows

def enforce_semicolon(query):
    lastchar = query[len(query)-1]
    if (lastchar != ';'): 
      return query + ';'
    else:
      return query


# def search(query_string):
#   conn=sqlite.connect('data.db')
#   cur = conn.cursor()
#   cur.execute(query_string)
#   conn.fetchall()
#   return rows

# connect()
# insert('Necromancer', 'Willy Gibson', 1987, 23415122)
# print(view())
# print(user_query('SELECT COUNT(*) FROM data'))
