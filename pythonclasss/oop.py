class Person:
    def __init__(self, name="default", age=22):
        self.name = name
        self.age = age

# create an instance after the class is defined
john = Person("John", 25)
print(john.age)

    