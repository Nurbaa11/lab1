#Sort the list alphabetically:
thislist1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist1.sort()
print(thislist1)

#Sort the list numerically:
thislist2 = [100, 50, 65, 82, 23]
thislist2.sort()
print(thislist2)

#Sort the list descending:(same with numbers)
thislist3 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist3.sort(reverse = True)
print(thislist3)

#Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist4 = [100, 50, 65, 82, 23]
thislist4.sort(key = myfunc)
print(thislist4)

#reverse
thislist5 = ["banana", "Orange", "Kiwi", "cherry"]
thislist5.reverse()
print(thislist5)

