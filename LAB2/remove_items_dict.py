#The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict1.popitem()
print(thisdict1)

#The del keyword removes the item with the specified key name:
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict2["model"]
print(thisdict2)

#The clear() method empties the dictionary:
thisdict5 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict5.clear()
print(thisdict5)