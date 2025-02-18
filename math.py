#1
import math
a = int(input())
s = math.pi
print (a*s/180)


#2
a = int(input()) 
b = int(input())
v = int(input())
j = (0.5 * ( b + v ) * a)
print (j)


# 3
import math
sides = int(input())
length = int(input())
x = (sides * (length ** 2)) / (4 * math.tan(math.pi / sides))
print(int(x))  # Convert after calculating



# 4
a = int ( input() )
b = float ( input() )
print(a*b)