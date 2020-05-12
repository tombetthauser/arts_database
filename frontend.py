from random import random
from random import seed
from tkinter.ttk import *
from tkinter import ttk
from tkinter import *
import webbrowser
import backend
import os

from random import seed
from random import random
from random import choice
seed(1)

questions_list = list(
  map(lambda name: 
      " ".join(name.split(" ")[1:]
    ), list(backend.all_columns())
  )
)
# print(questions_list)

def random_question():
  # sequence = [i for i in range(len(questions_list))]
  question = choice(questions_list)
  while (question.split(" ")[0] == "blank"):
    question = choice(questions_list)
  return question

def clear_all():
    results_box.delete(0, END)
    query_text.set("")

def all_columns():
  results_box.delete(0, END)
  for row in backend.all_columns():
    results_box.insert(END, row)

def all_rows():
  results_box.delete(0, END)
  for row in backend.all_rows():
    print(type(row))
    results_box.insert(END, row)

# def save_results():
#   print('-------------')
#   print(query_text.get())
#   print(type(query_text.get()))
#   print('-------------')
#   os.system(f"echo `{str(query_text.get())}` >> saved_queries.txt")
#   for ele in results_box.get(0, END):
#     os.system(f"echo `{e}` >> saved_queries.txt")
#   # os.system(f'echo "{results_box.get(ACTIVE)}" >> saved_queries.txt"')

def run_query():
  results_box.delete(0, END)
  for row in backend.user_query(query_text.get()):
    results_box.insert(END, str(row))

def show_example():
  results_box.delete(0, END)
  q1 = random_question()
  q2 = random_question()
  query_text.set(f"SELECT `{q1}`, `{q2}` FROM data ORDER BY `{q1}`;")

window = Tk()
# SELECT `What is your ethnicity / race?`, `Do you feel you were generally welcomed and embraced by the art world this past year?` FROM data ORDER BY `What is your ethnicity / race?`;
# SELECT `What 5 - 15 key words would you currently associate with your artwork, subject matters, mediums etc? Separate with commas. (i.e. figurative, muted color, social issues, air brush, interdisciplinary etc.)` FROM data WHERE `1: What is your gender?` LIKE `% emale %`;
window.title("Arts Database Explorer 1.0")
window.resizable(width=False, height=False)
window.configure(bg='#dedede')
window.geometry('1050x760')

Label(window, bg="#dedede", height=1).grid(row=0, column=0, columnspan=11)
Label(window, bg="#dedede", width=2).grid(row=0, column=0, rowspan=15)

Label(window, 
  text="Arts Database Explorer 1.0", 
  font='Times 25', 
  relief=SUNKEN, 
  borderwidth=6,
  fg="black", 
  bg="white", 
  width=73, 
  anchor=W, 
  padx=20, 
  pady=20, 
).grid(row=1, column=1, columnspan=9)

Label(window, bg="#dedede", height=1).grid(row=2, column=0, columnspan=11)

Label(window, 
  text="A desktop explorer for the State of the Arts 2019 survey results.", 
  font='Times 16', 
  relief=SUNKEN, 
  borderwidth=4,
  fg="black", 
  bg="white", 
  width=119, 
  anchor=W, 
  padx=20, 
  pady=10, 
).grid(row=3, column=1, columnspan=9)

Label(window, bg="#dedede", height=1).grid(row=4, column=0, columnspan=11)

Button(window, 
  highlightbackground='#777',
  text='VIEW ALL COLUMNS', 
  command=all_columns,
  cursor='hand2',
  anchor=W,
  width=18,
).grid(row='5', column='1')

Button(window, 
  highlightbackground='#64935e',
  text='RUN QUERY', 
  command=run_query,
  cursor='hand2',
  anchor=W,
  width=18,
).grid(row='5', column='3')

Button(window, 
  highlightbackground='#935e5e',
  text='CLEAR QUERY', 
  command=clear_all,
  cursor='hand2',
  anchor=W,
  width=18,
).grid(row='5', column='5')

Button(window, 
  highlightbackground='#777',
  command=show_example,
  text='RANDOM QUERY', 
  cursor='hand2',
  anchor=W,
  width=18,
).grid(row='5', column='7')

# Button(window, 
#   highlightbackground='#777',
#   command=save_results,
#   text='SAVE RESULTS', 
#   cursor='hand2',
#   anchor=W,
#   width=18,
# ).grid(row='5', column='7')

Button(window, 
  highlightbackground='#777',
  command=window.destroy,
  cursor='hand2',
  text='CLOSE', 
  anchor=W,
  width=18,
).grid(row='5', column='9')

Label(window,
  text="Enter your SQL query here:",
  font='Times 16',
  bg='#dedede',
  pady=15,
  anchor=W,
  width=23,
).grid(row='7', column='1')

query_text = StringVar()
Entry(window, 
  textvariable=query_text, 
  highlightthickness=0,
  borderwidth=10,
  relief=FLAT, 
  width=108, 
).grid(row=8, column=1, columnspan=9)

Label(window,
  text="Below are your query results:",
  font='Times 16',
  bg='#dedede',
  anchor=W,
  width=23,
  pady=15,
).grid(row=10, column=1)

results_box = Listbox(window,
  highlightthickness=0,
  borderwidth=10,
  relief=FLAT, 
  height= 18, 
  width=108, 
)
results_box.grid(row=11, column=1, columnspan=9)

Label(window, bg="#dedede", height=0, pady=1).grid(row=12, column=0, columnspan=11)

def callback(url): webbrowser.open_new(url)

link1 = Button(
    window,
    text='Visit Survey Page',
    highlightbackground='#bbb',
    cursor='hand2',
    anchor=W,
    width=18,
)
link1.bind("<Button-1>", lambda e: callback("http://sotasurvey.org/"))
link1.grid(row=13, column=1)

link2 = Button(
    window,
    text='GitHub Project Page',
    highlightbackground='#bbb',
    cursor='hand2',
    anchor=W,
    width=18,
)
link2.bind("<Button-1>", lambda e: callback("https://github.com/tombetthauser/arts_database"))
link2.grid(row=13, column=3)

link3 = Button(
    window,
    text='Learn Basic SQL',
    highlightbackground='#bbb',
    cursor='hand2',
    anchor=W,
    width=18,
)
link3.bind("<Button-1>", lambda e: callback("https://www.w3schools.com/sql/"))
link3.grid(row=13, column=5)

window.mainloop()