from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
# from tkinter.ttk import *
import webbrowser




window = Tk()

window.title("Arts Database Explorer 1.0")
window.geometry('1050x760')
window.configure(bg='#dedede')
window.resizable(width=False, height=False)

Label(window, bg="#dedede", height=1).grid(row=0, column=0, columnspan=11)

Label(window, bg="#dedede", width=2).grid(row=0, column=0, rowspan=15)

Label(
  window, 
  text="Arts Database Explorer 1.0", 
  width=73, 
  fg="black", 
  bg="white", 
  font='Times 25', 
  relief=SUNKEN, 
  anchor=W, 
  padx=20, 
  pady=20, 
  borderwidth=6
).grid(row=1, column=1, columnspan=9)

Label(window, bg="#dedede", height=1).grid(row=2, column=0, columnspan=11)

Label(
  window, 
  text="A desktop explorer for the State of the Arts 2019 survey results.", 
  width=119, 
  fg="black", 
  bg="white", 
  font='Times 16', 
  relief=SUNKEN, 
  anchor=W, 
  padx=20, 
  pady=10, 
  borderwidth=4
).grid(row=3, column=1, columnspan=9)

Label(window, bg="#dedede", height=1).grid(row=4, column=0, columnspan=11)

Button(
  window, 
  text='VIEW ALL COLUMNS', 
  highlightbackground='#777',
  width=18,
  anchor=W,
  cursor='hand2',
).grid(row='5', column='1')

Button(
  window, 
  text='RUN QUERY', 
  highlightbackground='#64935e',
  width=18,
  anchor=W,
  cursor='hand2',
).grid(row='5', column='3')

Button(
  window, 
  text='CLEAR QUERY', 
  highlightbackground='#935e5e',
  width=18,
  anchor=W,
  cursor='hand2',
).grid(row='5', column='5')

Button(
  window, 
  text='SAVE RESULTS', 
  highlightbackground='#777',
  width=18,
  anchor=W,
  cursor='hand2',
).grid(row='5', column='7')

Button(
  window, 
  highlightbackground='#777',
  command=window.destroy,
  cursor='hand2',
  text='CLOSE', 
  anchor=W,
  width=18,
).grid(row='5', column='9')

# Label(window, height=1, bg='#dedede').grid(row='6', column='0', columnspan=11)

Label(
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

Label(
  text="Below are your query results:",
  font='Times 16',
  bg='#dedede',
  pady=15,
  anchor=W,
  width=23,
).grid(row=10, column=1)

Listbox(window,
  highlightthickness=0,
  borderwidth=10,
  relief=FLAT, 
  height= 18, 
  width=108, 
).grid(row=11, column=1, columnspan=9)

Label(window, bg="#dedede", height=0, pady=1).grid(row=12, column=0, columnspan=11)

def callback(url): webbrowser.open_new(url)

link1 = Button(
    window,
    highlightbackground='#bbb',
    cursor='hand2',
    text='Visit Survey Page',
    anchor=W,
    width=18,
)
link1.bind("<Button-1>", lambda e: callback("http://sotasurvey.org/"))
link1.grid(row=13, column=1)

link2 = Button(
    window,
    highlightbackground='#bbb',
    cursor='hand2',
    text='GitHub Project Page',
    anchor=W,
    width=18,
)
link2.bind("<Button-1>", lambda e: callback("https://github.com/tombetthauser/arts_database"))
link2.grid(row=13, column=3)

link3 = Button(
    window,
    highlightbackground='#bbb',
    cursor='hand2',
    text='Learn Basic SQL',
    anchor=W,
    width=18,
)
link3.bind("<Button-1>", lambda e: callback("https://www.w3schools.com/sql/"))
link3.grid(row=13, column=5)

window.mainloop()
