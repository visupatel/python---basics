# print() statement(output)
print("Hello world")
print("Visha")


# For continue line because python statements are end with a new line.
str = "1"\
        "2"\
        "3"
        
print(str)         # 123

# [],{} or () do not need to use '\'.

fruits = ["Banana","Apple",
          "Watermelan",
          "Orange"]
print(fruits)



# Quotes

# single(')
word = 'word'
print(word)

# Double(")
name = "Visha Patel"
print(name)

# triple(''' or """)
sentence = """I am Learning 
Python Tutorial
from tutorialsPoint"""
print(sentence)



# Input
name = input("Enter your name : ")
print(name)


# Multiline statement on a single line(';' is used for it)
a = 10; b = 30; c = 20 ; print(a+b+c)




# Variables

# Create
name = "Visha"
age = 21
cgpa = 7.96
passed = True

# Print
print(name)
print(age)
print(cgpa)
print(passed)

# Delete
del name
print(name)       # give an error 'name' is not defined

# case-sensitivity
age = 21
Age = 50
print("age:",age)
print("Age:",Age)


# Multiple assignment
# 1
"""a = 10
b=10
c= 10 also written as """
a = b = c = 10
print(a,b,c)

# 2
"""a = 10
b=20
c= 30 also written as """
a,b,c = 10,20,30
print(a,b,c)





# Data type

# Numeric data type
a = 10
print(type(a))       # int

b = 10.2
print(type(b))       # float

c = 1 + 2j
print(type(c))        # complex


# String data type
str = "Hello"
print(type(str))

# Sequence data type
info1 = ["visha",21, 7.96] 
print(type(info1))

info2 = ("visha",21, 7.96)
print(type(info2))

num = range(5)
print(type(num))

# Dictionary data type
info = {"name" : "visha",
        "age" : 21,
        "cgpa" : 7.96
}
print(type(info))

# set data type
fruits = {"Mango","Apple","Orange"}
print(type(fruits))

# None type
a = None
print(type(a))



# Type conversion or explicit casting(need to change manually)
a = int("2")      # manuaaly change in int
b = float(4)
c = str(5)

d = int(True)
e = float(True)
f = str(True)
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))

print(d)
print(type(d))
print(e)
print(type(e))
print(f)
print(type(f))


# Implicit or automatic casting
a = 10
b = 10.5
c = a + b          # automatically change in float
print(c)
print(type(c))

a = True           # True = 1
b = 10.5
c = a + b          # automatically change in float
print(c)
print(type(c))




