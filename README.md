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

A sample stand-alone html map page generated after running the maps generator command line tool.
[click here to check out this sample map](https://tombetthauser.github.io/python_map/index.html)


***

# How to Use the Tool:
1. Download and run the seperate **arts_installer** tool linked [here](https://tombetthauser.github.io/arts_installscript/installer.sh)
2. Open your command line application (Terminal on MacOS), paste the following and hit enter to run the installer.
```
bash ~/Downloads/installer.sh
```
3. Install the Chromium tool in your Chrome web browser.
4. Download this GitHub project with the link above.
5. Paste the following in your command line and hit enter.
```
python3 ~/Downloads/arts_dataexplorer/frontend.py
```
6. You should see the application window pop open.
```
The data is all yours, explore it and discover something cool!
```
***  

# Project Details
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/SQLite370.svg/1024px-SQLite370.svg.png" height="150px">

This project was built with **Python** using the **SQLite3**, and **TkInter** libraries to interface with the data and create the desktop graphical user interface. The installer was written specifically for this project in **bash** shell script.

This was originally developed as two day project by [Tom Betthauser](http://www.tombetthauser.com/) in 2020.  

***
