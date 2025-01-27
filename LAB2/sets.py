#Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# A set can contain different data types:
set1 = {"abc", 34, True, 40, "male"}
print(set1)

thisset1 = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset1)

#add
thisset2 = {"apple", "banana", "cherry"}
thisset2.add("orange")
print(thisset2)

