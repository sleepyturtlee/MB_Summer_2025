class Cat:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return("Cat named " + self.name)

class Owner:
    def __init__(self, cat):
        self.cat = cat
    
    def __str__(self):
        return("Owner of Cat named " + self.cat.name)

cat1 = Cat("Whiskers")     
owner = Owner(cat1)            
print(owner.cat.name)     
print(owner)


"""import random
import math
print(random.randint(1, 10))

def roll_die():
    return random.randint(1, 6)

print(math.sqrt(16))"""



"""class Note:
    def __init__(self, content):
        self.content = content

    def show(self):
        print(f"Note: {self.content}")

class Notebook:
    def __init__(self):
        self.notes = []  # list to hold Note objects

    def add_note(self, note):
        self.notes.append(note)
    

# Example usage:
note1 = Note("Buy milk")
note2 = Note("Finish homework")

notebook = Notebook()
notebook.add_note(note1)
notebook.add_note(note2)"""

"""""from re import S
from turtle import title
from xml.etree.ElementTree import tostring
from pprint import pprint

class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says woof!")

# 9: Name of class is Dog
# 10: __init__ is the constructor which initializes different atributes/member vars of the class, and bark is a member function. they're tech. both member functions
# 11: self refers to the object itself
# 12: we can call bark by writing dog_var.bark()

strawberry = Dog("Strawberry")
strawberry.bark()"""

"""errors:
    1. indentation
    2. self should be the first parameter of every class method in python
    3. If you're trying to write the "Cat" class, maybe capital "C". All classes have to be capitalized
"""
"""class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(self.name + " says meow!")

blueberry = Cat("blueberry")
blueberry.meow()"""""

"""fruits = ["apple", "banana", "cherry", "date"]
person = {
    "name": "Bob",
    "age": 25,
    "city": "Chicago"
}

#1
print(fruits[2])

#2
print(person["age"])

#3: An error will occur (key that doesn't exist)
# person["hi"]

#4: dict.get(key) doesn't crash your program if the key doesn't exist.
print(person.get("hi"))

#5: Better to use dict.get("key") instead of dict["key"] when 

word = "hello"
print(word.upper())
# var word is a string
print(type(word))
# .upper() modifies strings ? maybe comes from data science where
# strings usually need to be formatted the same way
#8: .lower()
"""
"""
class Smartphone:
    def __init__(self, brand, model, storage):  # Class constructor
        self.brand = brand  # Initializes brand
        self.model = model  # Initializes model
        self.storage = storage  # Initializes storage

    def display_info(self):  # Method to display smartphone info
        print(f"Smartphone: {self.brand} {self.model}, Storage: {self.storage}GB")


# Creating two objects
my_phone = Smartphone("Apple", "iPhone 13", 128)
your_phone = Smartphone("Samsung", "Galaxy S22", 256)

# Using a method to display info about the phones
my_phone.display_info()  # Outputs -> Smartphone: Apple iPhone 13, Storage: 128GB
your_phone.display_info()  # Outputs -> Smartphone: Samsung Galaxy S22, Storage: 256GB


class Cow:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def moo(self):
        print("Moo")"""


"""
What I learned:
    1. All functions in a class must take in self as the first parameter
    2. member variables must be referred to as self.(var name)
    3. member vars can be named anything as long as it starts with self
"""

"""
class Book:
    # constructor
    def __init__(
        self, title="Milennium Falcon", author="George Lucas", year: int = 1970
    ):
        self.title = title
        self.author = author
        self.year = year

    def display_book(self):
        print(self.title)

    def describe(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")

    def is_classic(self):
        if self.year < 1970:
            return True
        return False

    def __str__(self):
        return self.__dict__


strawberry = Cow("Strawberry", "7", "Spotted")
strawberry.moo()
star_wars = Book("Star Wars", "George Lucas", 1987)
star_wars.display_book()
star_wars.describe()
print(star_wars.is_classic())
print(star_wars.__dict__)
new_star_wars = Book()
new_star_wars.describe()"""


"""student = {
    "Name": "Little Bob Junior",
    "Age": 1,
}

print(student.keys())
student["Little Bob Junior"] = 19
print(student)

student["grade"] = "A"
# print(student["school"])"""

"""country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome" 
}

# print dictionary keys one by one
for country in country_capitals:
    print(country)

print("----------")

# print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)"""

"""
# Creating a dictionary
country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Naples", 
  "England": "London",
  "Japan": "Hokkaido"
}

# Change value of "Italy" key to "Rome"
country_capitals["Italy"] = "Rome"
print(country_capitals)

country_capitals["Japan"] = "Tokyo"
print(country_capitals)

country_capitals["China"] = "Beijing"
print(country_capitals)

# deleting item
del country_capitals["United States"]
print(country_capitals)





# Printing the dictionary
# print(country_capitals) 
# try: 
#     print(country_capitals["Italy"])
# except:
#     print("Key does not exist!")

# print(country_capitals.get("United States"))
"""
