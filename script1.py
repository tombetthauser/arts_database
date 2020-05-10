from tkinter import *
from tkinter import ttk
import webbrowser

def callback(url):
    webbrowser.open_new(url)
    ## To open local files:
    # webbrowser.open_new(r"file://c:\test\test.csv")


window = Tk()

window.title("Arts Database Explorer 1.0")
window.geometry('1050x750')
window.configure(bg='#dedede')
window.resizable(width=False, height=False)

# link1 = Label(window, text="Google Hyperlink", fg="blue", cursor="hand2")
# link1.pack()
# link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))
# link1.grid(row=4, column=0)

# title_style = ttk.Style()
# title_style.configure("MainTitle", foreground="red", background="black")

l0 = Label(window, text="Arts Database Explorer 1.0", width=65, fg="black", bg="white", font='Times 25', relief=SUNKEN, anchor=W, padx=20, pady=20, borderwidth=6)
l0.pack(padx=30, pady=[20,10])
l0.pack(fill=X, padx=[35,35])

l0 = Label(window, text="A desktop explorer for the State of the Arts 2019 survey results.", width=65, fg="black", bg="white", font='Times 16', relief=SUNKEN, anchor=W, padx=20, pady=15, borderwidth=4)
l0.pack(padx=30, pady=[0,20])
l0.pack(fill=X, padx=[35,35])
# l0.grid(row=1, column=1)

# close = Button(window, text="CLOSE", width=12)
# close.pack(side=LEFT, pady=[20,20], padx=[35,35])

# close2 = Button(window, text="CLOSE", width=12)
# close2.pack(side=LEFT, pady=[20,20], padx=[35,35])

# l1 = Label(window, text="Enter your SQL query here:")
# l1.grid(row=0, column=0)

# l2 = Label(window, text="Below are your query results:")
# l2.grid(row=2, column=0)

# query_text = StringVar()
# e1 = Entry(window, textvariable=query_text, width=80)
# e1.grid(row=1, column=0)

# result_box = Listbox(window, height=10, width=50)
# result_box.grid(row=3, column=0, rowspan=6, columnspan=1)

# scroll_bar = Scrollbar(window)
# scroll_bar.grid(row=3, column=1, rowspan=6)

# result_box.configure(yscrollcommand=scroll_bar.set)
# scroll_bar.configure(command=result_box.yview)

window.mainloop()
