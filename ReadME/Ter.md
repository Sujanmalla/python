# python -m venv env 

This command creates a virtual environment named env.

🔹 Virtual Environment = a separate Python world

It keeps your project’s packages separate from your system Python.

✔Breakdown of the command
- Part	     - Meaning
- python	 -Runs Python
- -m	     -Run a module as a script
- venv	     -The module that creates virtual environments
- env	     -The name of the virtual environment folder



# .\env\Scripts\Activate.ps1

🔹 What it does

- Activates your virtual environment in PowerShell

- Changes your Python and pip to use the ones inside env

- Changes the terminal prompt to show (env) at the start, meaning the environment is active.
 

 Part	 Meaning
- .	     = Current directory
- \env\Scripts\Activate.ps1	 =Path to the PowerShell activation script inside your virtual environment


# pip install django

- pip = Python Package Installer

- It is used to install Python libraries or packages from the internet (PyPI - Python Package Index).

- Example packages: Django, Flask, NumPy, Pandas, etc.

# django-admin startproject puddle . 
 It creates a new Django project named puddle.

- A "project" is the main container that holds everything for your website:

- settings

- URLs

- apps

- templates

- database configuration

- Python files

- The dot (.) means create the project in the current folder instead of creating a new folder


# cd puddle
cd = Change Directory

It is used to move inside a folder.

This means:

 Go inside the folder named puddle.



You do not need to write cd puddle when you use the last dot.

Why?

Because the dot (.) tells Django:

 “Create the project in the folder where I already am.”

So Django will NOT create an outer folder named puddle.



# ls
ls = List Files

It is used to show all files and folders inside the current directory.

Example:


# python manage.py makemigrations

“Look at my models.py file and prepare database changes.”

In simple words:

It converts your Python models into migration files.

Migration files are instructions for creating or updating database tables.


# python manage.py migrate
 
migrate applies the database changes that Django created during makemigrations.

In simple words:

 It creates or updates database tables.

 # python manage.py runserver

\This command starts the Django development server.

It lets you run your website locally on your computer.

You can see your website in a browser at http://127.0.0.1:8000/