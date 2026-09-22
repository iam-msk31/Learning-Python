 
  ###  --->   Python Basics   <---  ###
# -------------------------------------------------------------------------------- 

#  What is Python?

# Python is a high-level, interpreted, general-purpose programming language.

#-->Features of Python :
# -> Easy-to-read syntax
# -> Free and open source
# -> Dynamically typed
# -> Object-oriented
# -> Cross-platform
# -> Large standard library
# -> Used in web development, automation, data science, AI, scripting, and more

# Example :
print("Hello world")

#-->Python Syntax
# Syntax means the rules used to write Python code.
# Python is case-sensitive:

name = "Quad"
Name = "AI"

print(name)
print(Name) # name and Name are different variables.

#-->Comments

# Comments are notes in the program. Python ignores them during execution.
# Single-line comments
# # This is a comment
# print("Hello")

# Comment after code
# print("Hello")  # Display Hello

# Multi-line comments
# Python does not have a special multi-line comment syntax, but triple-quoted strings are commonly used:

"""
This is a multi-line note.
Python treats it as a string.
"""

# The print() Function
# The print() function displays information on the screen.
print("Hello") # output is Hello
print(100) # output is 100
print(10 + 5) #output is 15

# Printing multiple values
name = "Sahil"
age = 20

print(name, age)# Sahil 20


# Variables
# A variable is a name used to store a value.
name = "MOHIT" # name is a variable "Samar" is its value
age = 20 # age is variable and 20 is its value
print(name) #MOHIT
print(age) #20

#Variable assignment
x = 10
y = 20

print(x)
print(y)

# Changing a variable
score = 50
print(score)

score = 80
print(score)

# Output:
# 50
# 80

# A variable can store a different type later because Python is dynamically typed:
value = 10
value = "Python"

# Multiple assignment
x, y, z = 10, 20, 30

print(x)
print(y)
print(z)

# Assigning the same value
# a = b = c = 100

# All three variables contain 100.
# Swapping variables
a = 10
b = 20

a, b = b, a

print(a)
print(b)


# Rules for Naming Variables
# A variable name:
# Can contain letters
# Can contain numbers
# Can contain underscores
# Cannot start with a number
# Cannot contain spaces
# Cannot be a Python keyword
# Is case-sensitive
