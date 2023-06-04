name = "Beau" #variables
age = 39
print(type(name))
print(isinstance(name, str))

age = float(2) #this class is known as constructor used to change datatypes and this process is known as casting

print(isinstance(age, int))
#if, else ,elif are examples of keywords and they cannot be used as variable names
agee = 8
agee+=8 #agee= agee+8
print(agee)
#STRING METHODS, these methods return a new modified string and do not change the original value of the string
print("""Krish is 
17 years old
.""")

print("Krish".lower())
print("Krish".islower())
print("Krish".isupper())
print("Krish".upper())
print("Krish".isalpha())
print("Krish sharma".title())
print("Krish sharma".join("Hi"))
print(len("krish"))
print("Kr" in "Krish")

#escaping is a method to add special characters to the string.
name  = "Be\"au"
print(name)
names = "Krish \nSharma"
print(names)
naming = "Krish"
print(naming[1:3])
print(naming[:3])
print(naming[1:])

#boolean 
done = False
print(type(done))
if done:
    print("Yes")
else:
    print("no")
#strings are false only when empty.
#number is false only at 0.
book1_read = True
book2_read = False
readany_book = any([book1_read, book2_read]) #any returns true if even 1 is true
readany_book1 = all([book1_read, book2_read]) #all returns true if both are true
print(readany_book)
print(readany_book1)

#COMPLEX NUMBERS
num1 = 2+3j
print(num1.real, num1.imag)

#built in functions
print(abs(-5.5)) #absolute
print(round(5.5)) #round off
print(round(5.55, 1)) #round offs to 1 place

#Enums are readable names bound to a name
from enum import Enum
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE.value)
#USER INPUT

age = input("What is your age")
print("Your age is" + age)

#CONTROL STATEMENTS
condition = True
if condition == True:
    print("The condititon")
    print("was True")
else:
    print("The Condition")
    print("was False")

#LISTS
dogs = ["roger", 1, "syd"]
print("Roger" in dogs)
print(dogs[2]) #INDEXING
dogs[2] = "Beau" #UPDATING AN ITEM
print(dogs)
dogs.append("Jane")
print(dogs)
dogs.extend(["Judah", 5]) # used to add multiple items (different from append)
dogs.remove("Judah")
dogs.pop() #removes the last item of the list
dogs.insert(2, "Jae") #to add an element at a particular position
print(dogs)

#TUPLES
names = ("Roger", "Syd")
print(names[0])
print(names.index("Syd"))
newNames = names + ("Beau", "Quincy")
print(newNames)

#DICTIONARIES
dog = {"name" : "Roger", "age": 8}
print(dog["name"])
print(dog.get("name"))
print(dog.pop("name"))
print(dog)
print(dog.popitem()) #deletes the last added key value pair
print("age" in dog)
print(list(dog.keys())) #returns the keys
print(dog.values()) #returns the values
print(dog.items()) #returns the dictionary
dog["food"] = "Cereal"
print(dog)

#SETS
set1 = {"Roger", "Syd"}
set2 = {"Roger"}
intersect = set1 & set2 #For intersection
print(intersect)
mod = set1 | set2 #For Union
print(mod)



"""
datatypes in python
complex for complex numbers 
bool for booleans
list for lists
tuple for tuples
dict for dictionaries
set for sets
"""

"""
= is assignment operator used to assign values
ARITHMETIC OPERATORS:
+, -, *, /, %, **, //
COMPARISON OPERATORS:
a=1
b=2
a == b #False
a !=b #True
a > b #False
a<=b #True
BOOLEAN OPERATORS:
condition1 = True
condition2 = False

not condition1 #False
condition1 and condition2 #False
condition1 or condition2 #True

BITWISE OPERATORS:
& performs binary AND
| performs binary OR
^ performs binary XOR
~ performs binary NOT
<< shift left
>> shift right

OTHER OPERATORS:
is (identity operator)
in (membership operator)

TERNARY OPERATORS:
return True if a>19 else False (Used to write if else statment in 1 line)
"""