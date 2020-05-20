# Arts Database Explorer Tool
### A Python-Based Desktop App for Arts Survey Data

A desktop application built in Python with TkInter and SQLite. Specifically to help artists, gallerists etc. explore the results from a census-style survey for visual artists and learn basic SQL.

<br><img src="https://www.spiffystores.com.au/blog/wp-content/uploads/2014/11/Search-Magnifying-Glass.jpg" height="250px">


***

### Non-Functional Goals:
1. Allow artists, gallerists or arts groups freely explore an d cross-reference data from the State of the Arts Survey 2019 (see separate repo for project).

### Current Functions / Features:
1. Convert the original survey data from csv to **SQLite** format.
2. Use **Pandas** library to make SQL queries through **Python**.
3. Create a minimal **Desktop GUI** using the **TkInter** library for users.

### Stretch Goals:
1. Export queries and query results to a text file as a record for users. 
2. Create a generalized mode or version of the app designed to interface with any csv.
3. Transition the project to a full stack web platform to bypass Apple's blocking exe version of app.
4. Create an exportable scatter plot mode that allows users to cross reference any two columns visually.


***


# Example Image:

<img src="https://raw.githubusercontent.com/tombetthauser/image_library/master/arts_database.png">


***

# How to Use the Tool:
1. Download the zipped version of the project folder 

 ---> [download arts_dataexplorer](https://github.com/tombetthauser/arts_dataexplorer/raw/master/program_files/other_files/arts_dataexplorer.zip)

2. Go to your downloads folder and double click the zip file to uncompress it.
3. Open the folder and double click the arts_explorer.command file to start the application.
4. Before starting this will check to see if you have access to the following tools:
```
• Python3 –– pre-installed on most Macs)
• Brew –– to help install Python3 if needed)
• TkInter –– python library for creating the graphic interface)
• SQLite –– python library for talking to the data
```
5. You might be asked for your main password if needed during these downloads
6. If you already have these set up you can directly open the application in Terminal.
```
python3 ~/Downloads/arts_dataexplorer/frontend.py
```
6. Either way the application should open up, click Sample Query to get started!
7. If the application ***doesn't open*** for any reason you can open it directly...
a. Second click the arts_dataexplorer folder and select "New Terminal at Folder"
b. Paste the following command into terminal and press enter.
```
bash arts_dataexplorer.command
```
8. If it still wont open for some reason give up and forget any of this ever happened!
9. You can always explore the data via the survey website [www.SotaSurvey.org/2019](http://www.sotasurvey.org/2019)
10. In any case if it did open, hooray!
```
You cant break anything, mess around freely and discover something cool in the data!
```
***  

# Project Details
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/SQLite370.svg/1024px-SQLite370.svg.png" height="150px">

This project was built with **Python** using the **SQLite3**, and **TkInter** libraries to interface with the data and create the desktop graphical user interface. The installer was written specifically for this project in **bash** shell script.

This was originally developed as two day project by [Tom Betthauser](http://www.tombetthauser.com/) in 2020.  

***
