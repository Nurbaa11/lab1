#remove()
thislist1 = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist1.remove("banana")
print(thislist1)

#pop()
thislist2 = ["apple", "banana", "cherry"]
thislist2.pop() #removes last item
thislist2.pop(1) #removes the item in the index 1
print(thislist2)

#del
thislist3 = ["apple", "banana", "cherry"]
del thislist3[0]
print(thislist3)

thislist4 = ["apple", "banana", "cherry"]
del thislist4 #removes all items

#clear
thislist5 = ["apple", "banana", "cherry"]
thislist5.clear()
print(thislist5)