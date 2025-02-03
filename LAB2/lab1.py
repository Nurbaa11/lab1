#Home
print("Hello World!")

#Syntax
if 5 > 2:
    print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!")

#Variables
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x, y, z)

#Multiple Values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

a = b = c = "Orange"
print(a)
print(b)
print(c)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Data types

x = "Hello World"   #str
x = 20   #int
x = 1j   #complex
x = ["apple", "banana", "cherry"]   #list
x = ("apple", "banana", "cherry")   #tuple
x = range(6)   #range
x = {"name" : "John", "age" : 36}   #dict
x = {"apple", "banana", "cherry"}   #set
x = frozenset({"apple", "banana", "cherry"})   #frozenset
x = True   #bool
x = b"Hello"   #bytes
x = bytearray(5)   #bytearray
x = memoryview(bytes(5))   #memoryview
x = None   #NoneType


#Numbers

#int
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#float
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#complex
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))




#Castings

#integers
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#floats
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#strings
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'



#Strings

print("Hello")
print('Hello')

print('He is called "Johnny"')

#strings are arrays
a = "Hello, World!"
print(a[1])

#Looping Through a String
for x in "banana":
    print(x)

#string length
a = "Hello, World!"
print(len(a))

#check string
txt = "The best things in life are free!"
print("free" in txt) #return BOOL

#check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt) #return BOOL



#Slicing
b = "Hello, World!"
print(b[2:5])


d = "Hello, World!"
print(d[:5])



#Upper Case
a = "Hello, World!"
print(a.upper())

#Lower Case
a = "Hello, World!"
print(a.lower())

#Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

#Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Placeholders and Modifiers
price = 59
txt = f"The price is {price} dollars"
print(txt)


#Escape Character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
# \'	---  Single Quote	
# \\	---  Backslash	
# \n	---  New Line	
# \r	---  Carriage Return	
# \t	---  Tab	
# \b	---  Backspace	
# \f	---  Form Feed	
# \ooo	---  Octal value	
# \xhh	---  Hex value


