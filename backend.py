import sqlite3

def all_columns():
  conn=sqlite3.connect('data.db')
  cur=conn.cursor()
  cur.execute('PRAGMA table_info(data);')
  rows=cur.fetchall()
  rows = map(lambda col: f'{col[0]}: {col[1]}', rows)
  conn.close()
  return rows

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

def format_query(query):
    query = str(query)
    lastchar = query[len(query)-1]
    if (lastchar != ';'): 
      return query + ';'
    else:
      return query

def user_query(query):
  query = format_query(query)
  conn=sqlite3.connect('data.db')
  cur=conn.cursor()
  cur.execute(query)
  rows=cur.fetchall()
  conn.close()
  return rows