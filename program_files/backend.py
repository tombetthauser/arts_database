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

def int_process(element):
  try:
    int(element)
    return f"`{element}`"
  except:
    try:
      int(element[0:len(element)-1])
      last_char = element[len(element)-1]
      num_string = element[0:len(element)-1]
      if (last_char == ','):
        return f"`{num_string}`,"
      elif (last_char == ';'):
        return f"`{num_string}`;"
      else:
        raise
    except:
      return f"{element}"


def format_query(query):
  query = str(query)
  lastchar = query[len(query)-1]
  if (lastchar != ';'): 
    query = query + ';'

  query = " ".join(map(lambda ele: int_process(ele), query.split(" ")))
  return query

    # try:
    #   int(query.split(" ")[1])
    #   # replace numbers with column names
    #   # return the new query
    # except: 
    #   # return the query

# in the processing of the csv --> sqlite3 to have integer column headings and make a seperate lookup dictionary for the question strings


def user_query(query):
  query = format_query(query)
  conn=sqlite3.connect('data.db')
  cur=conn.cursor()
  cur.execute(query)
  rows=cur.fetchall()
  conn.close()
  return rows
