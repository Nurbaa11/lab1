#Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Add Items
   #Convert into a list: 
thistuple1 = ("apple", "banana", "cherry")
y1 = list(thistuple1)
y1.append("orange")
thistuple1 = tuple(y1)

#Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y2 = ("orange",)
thistuple += y2

print(thistuple)