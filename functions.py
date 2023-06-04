#FUNCTIONS

def hello(name, age ): #parameters are the values we pass in function definition
    print("Hello! " + name +  ", you are " + str(age) + " years old.")

hello("Beau",41) #arguments are values passing in function call statement
hello("Krish",17)

def change(value):
    value["name"]="Krish"

val={"name":"Beau"}
change(val)
print(val)


#VARIABLE SCOPE
age = 8 #global variable can be used in the function

def test():
    print(age)

test()
print(age)

def test():
    age=8 #local variable
    print(age)

test()
print(age)

#NESTED FUNCTIONS
def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)

talk('I am going.')


#NONLOCAL allows u to access variable values defined outside the function in the function.
def count():
    count=0

    def increment():
        nonlocal count
        count = count+1
        print(count)

    increment() 
count()

#objects
#everything in python is an object
age = 8
print(age.real)
print(age.imag)
print(age.bit_length())


items = [1, 2]
items.append(3)
items.pop()
print(id(items))

#LOOPS
#while loop
count = 0
while count <10:
    count+=1
    print(count)

#for loop
for item in range(15):
    print(item)

items = [1, 2, 3, 4]
for index, item in enumerate(items): #enumerate reutrns the index and the item itself
    print(index, item)


#JUMP STATEMENTS
#Continue stops the current iteration of the loop and continues with the next one
#Break just stops the loop altogether.
items = [1, 2, 3, 4]
for item in items: 
    if item == 2:
        continue
    print(item)


items = [1, 2, 3, 4]
for item in items: 
    if item == 2:
        break
    print(item)


#classes
class Animal:
    def walk (self):
        print("Walking")

class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

roger = Dog("Roger", 8)
print(type(roger))
print(roger.age)
roger.walk()


#modules
""" some libraries--
math for math utilities
re for regular expressions
json to work with JSON
datetime to work with dates
sqlite3 to use SQLite
os for Operating System Utilities
random for random number generation
statistics for statistics utilities
requests to perform HTTP network requests
http to create HTTP servers
urllib to manage URLs """

import math

print(math.sqrt(4))

from math import sqrt #other method

print(sqrt(4))

#Accepting Arguments
import sys
print(sys.argv)

#lambda function-- functions having no name and only have one expression in their body.

lambda num : num * 2

multiply =  lambda a, b : a * b

print(multiply(2, 4))

#map(), filter(), reduce()
numbers = [1, 2, 3]

def double(a):
    return a * 2

result = map(double, numbers)  #map is used when u use a function and a list in function call so the map() function returns a list

print(list(result))

""" filter() takes an iterable sequence and returns another iterable sequence """

numberss = [1, 2, 3]
def isEven(n):
    return n % 2 == 0

result = filter(isEven, numberss)

print(list(result))

""" reduce() is used to calculate a value out of a sequence """
from functools import reduce
expenses = [
    ('Dinner', 80),
    ('Car Repair', 120)
]

sum = reduce(lambda a, b: a[1] + b[1], expenses)

print(sum)

#Recursion
""" A function can call itself(Recursion) """
def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(factorial(5))

#Decorators- A way to change/alter working of a function
def logtime(func):
    def wrapper():
        print("Before")
        val = func()
        print("after")
        return val
    return wrapper

@logtime
def hello():
    print("Hello")

hello()

#Docstrings
""" It is a method to just give better understanding or knowledge to readers of the code """
""" Started by three quotes and ended by three. """

#Annotations
""" python is dynamically typed and to specify a datatype of a variable we used annotations """
def increment(n: int) -> int:
    return n+1

#Exceptions
""" try and except are used for errors
try tests a block of code for errors and except handles the error """

try:
    result = 2 / 0
except ZeroDivisionError:
    print("Cannot Divide by Zero!")
finally: 
    result = 1

print(result)

#Third party packages using pip

#LIST COMPRESSIONS

numbers = [1, 2, 3, 4, 5]

numbers_power_2 = [n**2 for n in numbers]
print(numbers_power_2)

""" to do the same thing by loop """
numbers_power_3 = []
for n in numbers:
    numbers_power_3.append(n**2)


#polymorphism 
class Dog:
    def eat(self):
        print("Eating dog food")

class Cat:
    def eat(self):
        print("Eating cat food")

animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()

#Operator Overloading
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return True if self.age > other.age else False
    
roger = Dog('Roger', 8)
syd = Dog('Syd', 9)

print(roger>syd)
        



