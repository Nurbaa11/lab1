#Print all items in the list, one by one:
thislist1 = ["apple", "banana", "cherry"]
for x in thislist1:
  print(x)

#Use the range() and len() functions to create a suitable iterable.
thislist2 = ["apple", "banana", "cherry"]
for i in range(len(thislist2)):
  print(thislist2[i])

#Print all items, using a while loop to go through all the index numbers
thislist3 = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist3):
  print(thislist3[i])
  i = i + 1

#A short hand for loop that will print all items in a list:
thislist4 = ["apple", "banana", "cherry"]
[print(x) for x in thislist4]