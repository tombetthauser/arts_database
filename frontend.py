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


state = {
    'QUESTIONS': ("Timestamp","What is your gender?","What is your ethnicity / race?","Do you currently identify as LGBTQ+?","What is your age?","How did you hear about this survey?","What 5 - 15 key words would you currently associate with your artwork, subject matters, mediums etc? Separate with commas. (i.e. figurative, muted color, social issues, air brush, interdisciplinary etc.)","Are there any questions you would add, remove or change in section 1?","How much of a priority was exhibiting your work this past year?","How many group exhibitions were you in this past year?","How many solo exhibitions did you have this past year?","How many exhibitions did you apply for this past year?","Roughly how much did you pay total in application fees for exhibitions this past year?","What kinds of exhibition spaces / venues did you show in this past year? (check any that apply)","Roughly how many times was your work written about in an online or print publication this past year? ","Roughly how many times was your work featured / re-posted by someone else on social media this past year?","How did your exhibition opportunities this year come about? (check any that apply)","How many shows / events / books etc. did you help organize this past year? (not related to job duties)","Did you have official gallery representation this past year? (listed officially on their website)","Were you given any kind of legal paperwork (contract, loan agreement, tax document etc.) by a gallerist, art dealer or collector this past year?","How much of a priority was applying for residencies or grants this past year?","How many residencies did you apply for this past year?","How many residencies did you attend this past year?","How many grants did you apply for this past year?","How many grants did you receive in total this past year?","Roughly how much did you receive in total grants this year?","Are there any questions you would add, remove or change in section 2?","How much of a priority was selling your art or art-related work this past year?","Who did you sell art or art-related work to this past year? (check any that apply or add other)","How did you make art-related sales this past year? (check any that apply)","Roughly how much money did you make from art-related sales this year?","What kinds of work did you sell this past year? Separate with commas. If none, leave blank. (i.e. paintings, etchings, t-shirts etc.)","How would you rate the overall treatment you received from the collectors / buyers you worked with this past year?","Did you use any of the following platforms to make sales this past year? Check any that apply.","How much of a priority was having studio visits for you this past year?","Roughly how many studio visits did you have this past year?","Whom did you have one or more studio visits this past year? (check any that apply or leave blank if none)","How did your studio visits this year come about? (check any that apply or leave blank if none)","Are there any questions you would add, remove or change in section 3?","How much of a priority was social media use for you / your studio this past year?","Roughly how often did you create Facebook posts related to your artwork or exhibitions this past year?","Did you use Facebook more or less this past year than the previous year?","Roughly how often did you create Instagram posts related to your artwork or exhibitions this past year?","Did you use Instagram more or less this past year than the previous year?","Did you pay for any social media promotion this past year? If so did it have a noticeable positive impact?","How well do you feel your primary social media platform served you / your studio practice this past year? (10 being the best possible score)","What aspects of your primary social media platform did you think worked well for you / your studio this past year? (i.e. public likes, follower counts, order of posts in feed etc.)","What aspects of your primary social media platform did you think worked poorly or were problematic for you / your studio this past year?","Did you maintain a personal art / studio website this past year (i.e. www .yourname .com etc.) that was not on a social media platform?","Did you maintain a personal art / studio website at any point during 2016?","What other resources did you use frequently this past year for finding art-related content? (check all that apply)","Are there any questions you would add, remove or change in section 4?","What type of work space did you use this past year? (check any that apply)","Roughly how large is your current personal work space?","How much did you pay for your most recent month of studio space rent?","On an average week how many days did you get to work in your studio this past year? (counting half or partial days)","On an average studio day how much time did you spend in your studio space? (working / reading / thinking etc.)","Are there any questions you would add, remove or change in section 5?","What types of jobs did you have this year?","Did you apply for or receive unemployment benefits or food stamps this year?","Roughly how many jobs did you apply for this year?","Roughly how much did you make in job-related income this year? (not including art sales)","Did you claim any art / studio expenses on any tax return filed this past year?","Are there any questions you would add, remove or change in section 6?","What is your highest level of education? Choose the most specific / appropriate answer.","Are you currently a student?","If you are currently a student what school do you attend?","List any past degrees you've completed. Include the schools and graduation years. Separate with commas and periods. (i.e. BS in Psychology, Iowa State, 2009. MFA in Digital Media, UC Santa Cruz, 2012 etc.)","How would you rate your educational experience overall? (1 being poor, 10 being exceptional)","Roughly how much do you currently owe in student loans? (if currently a student estimate loans upon graduation)","Roughly how much was your most recent monthly student loan payment?","Are there any questions you would add, remove or change in section 7?","What neighborhood and city do you currently live in? Separate with commas. (i.e. Korea Town, Los Angeles)","What neighborhood and city did you live in at the end of 2016?","What are the most important benefits of your current city or neighborhood? Separate with commas. (i.e. diverse population, affordability, safety, good weather)","Are there any questions you would add, remove or change in section 8?","How much of a priority was visiting galleries / museums for you this past year?","Roughly how many gallery receptions / openings did you attend in total this past year?","Roughly how many times did you attend an art fair or biennial this past year?","How many new galleries can you personally think of that opened this past year in your city? (don’t overthink it)","How many galleries can you personally think of that closed this past year in your city? (don’t overthink it)","Are there any questions you would add, remove or change in section 9?","What schools did you teach for this past year? (optional)","How many classes did you teach in your most recent semester?","How many campuses did you teach at in your most recent semester?","How would you rate the overall work environment of your school or schools this past year?","Were you a part of a union this past year?","What additional duties aside from teaching did you perform for your school or schools this past year? Separate with commas, if none leave blank.","Were you explicitly paid for these extra duties?","Are there any questions you would add, remove or change in section 10?","Roughly how long did you spend filling out this survey?","Do you feel you were generally welcomed and embraced by the art world this past year?","Do you feel that you or your career may have been significantly negatively effected by any type of discrimination or bias this past year?","Are there any arts institutions, galleries etc. that you would like to anonymously cite for outstanding service to artists or communities this past year? Separate by commas, if none leave blank.","Are there any arts institutions, galleries etc. that you would like to anonymously cite for harming artists or communities this past year? Separate by commas, if none leave blank.","Are there any questions you would add, remove or change in this final section?","Are there any sections you would add or remove completely from this survey?","Do you have any final thoughts regarding this survey?","blank column 1","blank column 2","blank column 3","blank column 4","blank column 5","blank column 6"),
    'current_query': None,
    'query_count': 0
}

questions_list = list(
  map(lambda name: 
      " ".join(name.split(" ")[1:]
    ), list(backend.all_columns())
  )
)

def random_question():
  question = choice(questions_list)
  while (question.split(" ")[0] == "blank"):
    question = choice(questions_list)
  return question

def clear_all():
    results_box.delete(0, END)
    query_text.set("")

def all_columns():
  results_box.delete(0, END)
  results_box.insert(END, 'Currently displaying all column names (which are numbers) from "data" table.')
  results_box.insert(END, '"Data" table is the only table used in this database.')
  results_box.insert(END, 'Use SQLite syntax and reference numbers rather than question text for all queries.')
  results_box.insert(END, 'Check out the "Sample Query" button above or "Learn Basic SQL" link below for help writing queries.')
  results_box.insert(END, '')
  results_box.insert(END, '-------------------------------------------------------')
  results_box.insert(END, '')
  for row in backend.all_columns():
    results_box.insert(END, f'{row.split(":")[0]}: {state["QUESTIONS"][int(row.split(":")[0])]}')

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

def translate_query(query_string):
  formatted_query = backend.format_query(query_string)
  query_split = formatted_query.split("`")
  translated_split = map(lambda ele: translate_element(ele), query_split)
  return list(translated_split)

def translate_element(element):
  try:
    int(element)
    return f"{int(element)}: {state['QUESTIONS'][int(element)]}"
  except:
    return element

def run_query():
  query = query_text.get()
  state["current_query"] = query
  results_box.delete(0, END)
  for ele in translate_query(query):
    if (len(ele) > 3):
      if (ele[0] == " "):
        results_box.insert(END, ele[1:len(ele)])
      else:
        results_box.insert(END, ele)

  results_box.insert(END, '')
  results_box.insert(END, '-------------------------------------------------------')
  results_box.insert(END, '')

  for row in backend.user_query(query):
    trimmed_row = str(row)[0:len(str(row))-1]
    if (trimmed_row[len(trimmed_row)-1] == ','):
      trimmed_row = trimmed_row[0:len(trimmed_row)-1]
    trimmed_row = trimmed_row + ")"
    results_box.insert(END, trimmed_row)

def show_example():
  results_box.delete(0, END)

  q1 = random_question()
  while ((state["QUESTIONS"][int(q1)][0:5] == "blank") or ("add, remove" in state["QUESTIONS"][int(q1)]) or (int(q1) == 97)):
    q1 = random_question()

  q2 = random_question()
  while ((state["QUESTIONS"][int(q2)][0:5] == "blank") or ("add, remove" in state["QUESTIONS"][int(q2)]) or (int(q2) == 97)):
    q2 = random_question()

  q3 = random_question()
  while ((state["QUESTIONS"][int(q3)][0:5] == "blank") or ("add, remove" in state["QUESTIONS"][int(q3)]) or (int(q3) == 97)):
    q3 = random_question()

  example_difficulty = state['query_count'] % 11

  if (example_difficulty == 1):
    query_string = f"SELECT `{q1}` FROM data ORDER BY `{q1}`;"
  elif (example_difficulty == 2):
    query_string = f"SELECT COUNT(*), `{q1}` FROM data GROUP BY `{q1}`;"
  elif (example_difficulty == 3):
    query_string = f"SELECT COUNT(*), `{q1}` FROM data GROUP BY `{q1}` ORDER BY `{q1}`;"
  elif (example_difficulty == 4):
    query_string = f"SELECT COUNT(*), `{q1}` FROM data GROUP BY `{q1}` ORDER BY COUNT(*);"
  elif (example_difficulty == 5):
    query_string = f"SELECT COUNT(*), `{q1}` FROM data GROUP BY `{q1}` ORDER BY COUNT(*) DESC;"
  elif (example_difficulty == 6):
    query_string = f"SELECT COUNT(*), `{q1}` FROM data GROUP BY `{q1}` ORDER BY COUNT(*) ASC;"
  elif (example_difficulty == 7):
    query_string = f"SELECT `{q1}`, `{q2}` FROM data;"
  elif (example_difficulty == 8):
    query_string = f"SELECT `{q1}`, `{q2}` FROM data ORDER BY `{q1}`;"
  elif (example_difficulty == 9):
    query_string = f"SELECT COUNT(*), `{q1}`, `{q2}` FROM data GROUP BY `{q1}`, `{q2}` ORDER BY COUNT(*) DESC;"
  elif (example_difficulty == 10):
    query_string = f"SELECT COUNT(*), `{q1}`, `{q2}`, `{q3}` FROM data GROUP BY `{q1}`, `{q2}`, `{q3}` ORDER BY COUNT(*) DESC;"
  else:
    query_string = f"SELECT `{q1}` FROM data;"
    
  state['query_count'] = state['query_count'] + 1
  state['current_query'] = query_string
  query_text.set(query_string)
  run_query()

window = Tk()

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
  text="A desktop explorer for the State of the Arts 2019 survey results. Built using Python3 with TkInter and SQLite3.", 
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
  text='SAMPLE QUERY', 
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

all_columns()
window.mainloop()
