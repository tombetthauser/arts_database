from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
# from tkinter.ttk import *
import webbrowser




window = Tk()

window.title("Arts Database Explorer 1.0")
window.geometry('1050x750')
window.configure(bg='#dedede')
window.resizable(width=False, height=False)

padrow0 = Label(window, text="", bg="#dedede", height=1)
padrow0.grid(row=0, column=0, columnspan=11)

padcol0 = Label(window, text="", bg="#dedede", width=2)
padcol0.grid(row=0, column=0, rowspan=15)

top_label = Label(window, text="Arts Database Explorer 1.0", width=73, fg="black", bg="white", font='Times 25', relief=SUNKEN, anchor=W, padx=20, pady=20, borderwidth=6)
top_label.grid(row=1, column=1, columnspan=9)

padrow1 = Label(window, text="", bg="#dedede", height=1)
padrow1.grid(row=2, column=0, columnspan=11)

subtitle_label = Label(window, text="A desktop explorer for the State of the Arts 2019 survey results.", width=119, fg="black", bg="white", font='Times 16', relief=SUNKEN, anchor=W, padx=20, pady=10, borderwidth=4)
subtitle_label.grid(row=3, column=1, columnspan=9)


# style = Style()
# style.configure('W.TButton', font=('calibri', 10, 'bold', 'underline'),
#                 foreground='black')

# close = Button(window, text="CLOSE", width=12, command=window.destroy, highlightbackground="#999", font="Arial 14")
# close.pack(side=BOTTOM, pady=[20,20], padx=[35,5])



# Style will be reflected only on
# this button because we are providing
# style only on this Button.
# ''' Button 1'''
# btn1 = Button(root, text='Quit !',
#               style='W.TButton',
#               command=root.destroy)
# btn1.grid(row=0, column=3, padx=100)

# ''' Button 2'''
# btn2 = Button(root, text='Click me !', command=None)
# btn2.grid(row= 1, column = 3, pady = 10, padx = 100)











# l1 = Label(window, text="Enter your SQL query here:")
# l1.grid(row=0, column=0)

# l2 = Label(window, text="Below are your query results:")
# l2.grid(row=2, column=0)

# query_text = StringVar()
# e1 = Entry(window, textvariable=query_text, width=80)
# e1.grid(row=1, column=0)

# result_box = Listbox(window, height=10, width=50)
# result_box.pack(fill=X)
# result_box.grid(row=3, column=0, rowspan=6, columnspan=1)

# scroll_bar = Scrollbar(window)
# scroll_bar.grid(row=3, column=1, rowspan=6)

# result_box.configure(yscrollcommand=scroll_bar.set)
# scroll_bar.configure(command=result_box.yview)

window.mainloop()








### LINKS

# def callback(url):
#     webbrowser.open_new(url)
#     ## To open local files:
#     # webbrowser.open_new(r"file://c:\test\test.csv")

# link1 = Label(window, text="Google Hyperlink", fg="blue", cursor="hand2")
# link1.pack()
# link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))
# link1.grid(row=4, column=0)

# title_style = ttk.Style()
# title_style.configure("MainTitle", foreground="red", background="black")
