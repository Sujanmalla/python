# Virtual Environment 
A virtual environment (virtual env) in Python is like a separate mini-Python workspace where you can install libraries without affecting your main system Python. 
                                   

A virtual environment (virtual env) in Python is like a separate mini-Python workspace where you can install libraries without affecting your main system Python.


# Benefit of Virtual Environments



- NO Version conflict 

- every project has  clean, separate libaries 

- Easy to manage project packages 

- Makes deployment easier 

- Keeps ypur system Python clean


# Pipenv 

Pipenv(often written as pip env ) is a tool in python tha t helps you manage:

- Virtual environments 
- Project dependencies(Pakages)
- Packages Version(using Pipfile.lock)

IT combines the power of pip + virtualenv into one simple tool.



pipenv is a packages manager in Python that automatically createsa virtual environmemt and installs packages in a clean, organzed way.


# what does PIpenv do 

- Create a virtual environment

- Install Flask inside that environment

- create a pipfile-> listes the pacakges you need 

- create a pipfile.lock -> locks exact version for stability

# MVT
Django follows the MVT architecture, which stands for:

M → Model
V → View
T → Template 

# Model
Represents the data or database structure.

Defines tables, fields, and data relationships.

Located in models.py.
```
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

```
# View
Handles business logic and data processing.

Connects models and templates.

Located in views.py.

```
from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

```
# Template

A template is an HTML file that defines the structure of the web page.

It can contain HTML, CSS, and Django template tags.

Templates separate the frontend (presentation) from the backend (Python code).

Django uses templates to render dynamic content.
```
myapp/
    templates/
        index.html
        about.html

```

# WSGI 
WSGI stands for Web Server Gateway Interface.

It is a standard interface between web servers and Python web applications/frameworks like Django or Flask.

It allows Python apps to communicate with web servers (like Apache, Nginx).

Without WSGI, Python apps cannot directly serve web requests.

# Why WSGI is Needed

Web servers (Apache, Nginx) don’t understand Python code directly.

WSGI acts as a bridge between the server and Python code.

Ensures compatibility between frameworks and servers.

```
myproject/
    wsgi.py

```

# ASGI
ASGI stands for Asynchronous Server Gateway Interface.

It is the modern version of WSGI.

Supports asynchronous communication (real-time features) like WebSockets, long-polling, or background tasks.

Allows Django and other Python frameworks to handle both HTTP and async protocols.

# Why ASGI is Needed

WSGI is synchronous, meaning it handles one request at a time per worker.

ASGI allows multiple requests simultaneously, perfect for chat apps, notifications, or real-time updates.
```
myproject/
    asgi.py 

```

# Templates vs Views in Django

Even if you use templates for the frontend, views are still necessary.

Why?

Template → Only defines how the page looks (HTML/CSS/JS).

View → Handles what data to send to the template and how to respond to user requests.

Without a view, the template cannot get data dynamically or respond to forms, buttons, or URLs


