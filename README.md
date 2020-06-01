# Arts Database Explorer Tool
### A Python-Based Desktop App for Arts Survey Data

A desktop application built in Python with TkInter and SQLite. Specifically to help artists, gallerists etc. explore the results from a census-style survey for visual artists and learn basic SQL.
 ---> [download arts_dataexplorer.zip](https://github.com/tombetthauser/arts_dataexplorer/raw/master/program_files/other_files/arts_dataexplorer.zip)

<br><img src="https://raw.githubusercontent.com/tombetthauser/image_library/master/data_explorer.png" height="250px">


***

### Non-Functional Goals:
1. Allow artists, gallerists or arts groups freely explore an d cross-reference data from the State of the Arts Survey 2019 (see separate repo for project).

### Current Functions / Features:
1. Convert the original survey data from csv to **SQLite** format.
2. Use **SQLite** library to make SQL queries through **Python**.
3. Create a minimal **Desktop GUI** using the **TkInter** library for users.

### Stretch Goals:
1. Export queries and query results to a text file as a record for users. 
2. Create a generalized mode or version of the app designed to interface with any csv.
3. Transition the project to a full stack web platform to bypass Apple's blocking exe version of app.
4. Create an exportable scatter plot mode that allows users to cross reference any two columns visually.


***


# Example Gif:

<img src="https://raw.githubusercontent.com/tombetthauser/arts_dataexplorer/master/program_files/other_files/arts_dataexplorer.gif">


***

# How to Use the Tool:
```
Note that for now this app is only set up to work with Unix based systems (MacOS and Linux).
Sorry in advance! 😕
```
1. Download the zipped version of the project folder...

 ---> [download arts_dataexplorer.zip](https://github.com/tombetthauser/arts_dataexplorer/raw/master/program_files/other_files/arts_dataexplorer.zip)

2. Go to your downloads folder and double click the zip file to uncompress it.
3. Open the folder and **double click the arts_explorer.command file to start** the application.
## If you encounter an issue...
1. If you get a popup after you double-click the application file about permissions need to be changed, open up your Terminal application (hit command + space, then type "Terminal", then hit enter).
2. Then paste the following code into your command line and hit enter...
```
chmod u+x ~/Downloads/arts_dataexplorer/arts_dataexplorer.command
```
3. Then enter the following, hit enter and confirm your password...
```
sudo spctl --master-disable
```
4. This will let the computer know you want to be able to open the app directly.
5. If you're a regular Terminal user make sure that file path there makes sense.
6. You can also open the file directly through Terminal with this command...
```
bash arts_dataexplorer.command
```
7. If it still wont open for some reason give up and forget any of this ever happened, this tool is still under construction!
8. **Please let me know if you have any trouble** so I can fix it!..
```
tombetthauser@gmail.com / twitter: @tombetthauser
```
## As it's opening up...
1. Before starting the application will check to see if you have access to the following tools...
```
• python3 –– pre-installed on most Macs
• brew –– to help install Python3 if needed
• tkinter –– python library for creating the graphic interface
• sqlite –– python library for talking to the data
```
2. You might be asked for your main password if needed during these downloads.
3. If you already have these set up you can directly open the application in Terminal...
```
python3 ~/Downloads/arts_dataexplorer/frontend.py
```

## Once you've got the application open...
1. Click Sample Query to get started and see what happens!
2. Start playing around with the SQL syntax and see how things change.
3. If the SQL Queries are confusing **don't be intimidated** they're actually very simple to figurea out. Just check out the link at the bottom of the app to pick up some of the basics :)
4. You can always explore a non-interactive version of the data via the survey website also. [www.SotaSurvey.org/2019](http://www.sotasurvey.org/2019)
```
You cant break anything so mess around freely. 🎉
Don't be intimidated and discover something cool in the data!
```
***  

# Project Details
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/SQLite370.svg/1024px-SQLite370.svg.png" height="150px">

This project was built with **Python** using the **SQLite3**, and **TkInter** libraries to interface with the data and create the desktop graphical user interface. The installer was written specifically for this project in **bash** shell script.

This was originally developed as two day project by [Tom Betthauser](http://www.tombetthauser.com/) in 2020.  

***
