#  OOP 

Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.


Advantages of OOP
- Provides a clear structure to programs
- Makes code easier to maintain, reuse, and debug
- Helps keep your code DRY (Don't Repeat Yourself)
- Allows you to build reusable applications with less code


# Class 
A class is like a blueprint or template for creating objects.
It defines what properties (attributes) and behaviors (methods) the objects will have. 


```
class Student:
    # attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

```


# Object

```
# create objects
student1 = Student("Lemon", 20)
student2 = Student("Alex", 22)

# use method
student1.greet()   # Hello, my name is Lemon and I am 20 years old.
student2.greet()   # Hello, my name is Alex and I am 22 years old.


```


#  Python __init__() Method

All classes have a built-in method called __init__(), which is always executed when the class is being initiated.
It is called automatically when you create an object.

The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created. 

``` 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

```

# The self Parameter 
The self parameter is a reference to the current instance of the class.

It is used to access properties and methods that belong to the class. 

```
class Student:
    def __init__(self, name, age):
        self.name = name   # self.name belongs to this object
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# create objects
student1 = Student("Lemon", 20)
student2 = Student("Alex", 22)

# call method
student1.greet()  # Hello, my name is Lemon and I am 20 years old.
student2.greet()  # Hello, my name is Alex and I am 22 years old.

```

# self 

self means "this object".

Whenever you create an object from a class, self lets that object store its own data and use its own methods.

```
class Student:
    def __init__(self, name, age):
        self.name = name   # stored in the object
        self.age = age     # stored in the object

```

now you can create object
```
s1 = Student("Lemon", 20)
s2 = Student("Alex", 22)

```

# Why Use self?
Without self, Python would not know which object's properties you want to access: 
```
class Person:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()
p2.printname()
```
It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class:

# Class Properties 

Class properties (also called class attributes) are variables that:

belong to the class itself
are shared by all objects of that class
 do NOT change from one object to another unless you change them in the class

 ```
 class Student:
    school = "Poco College"   # ← class property

    def __init__(self, name):
        self.name = name  # ← object property

 ```

 # Object Properties
 Object properties are variables that belong to a specific object, not the class.

Every object has its own copy
They can be different for each object
Stored using self
```
class Student:
    def __init__(self, name, age):
        self.name = name   # object property
        self.age = age     # object property

```

# Class Method
Methods are functions that belong to a class. They define the behavior of objects created from the class. 

```
class Student:
    school = "Poco College"   # class property

    @classmethod
    def show_school(cls):
        return cls.school

```

# Python Inheritance 

Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

```
class Animal:   # Parent class
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):   # Child class inheriting Animal
    pass

d = Dog()
d.sound()       # Output: Animal makes a sound

```
# Recursion
Recursion is when a function calls itself to solve a problem.

A recursive function must have a base case to stop, otherwise it will run forever.

```
def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    else:
        return n * factorial(n-1)  # recursive call

print(factorial(5))   # Output: 120

```

output
```
factorial(5)
= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1
= 120

```
It’s useful for problems that can be broken into smaller similar problems.
# Python Inner Classes
Python Inner Classes (also called Nested Classes) are classes defined inside another class.

They help to organize code, create logical grouping, and represent a has-a relationship.

```
class Person:

    class Address:      # Inner class
        def __init__(self, city):
            self.city = city

    def __init__(self, name, city):
        self.name = name
        self.address = Person.Address(city)

p = Person("John", "Pokhara")
print(p.name)
print(p.address.city)

``` 