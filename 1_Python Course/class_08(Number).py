x = 2
y = 3
z = 4

#never use this format
print(x + y * z)

#Add () which you want to perform first

print(( x + y ) * z)
print(x + ( y * z ))

#Never prform such operation in code base
print(40 + 2.23)

#Datatype of both the values shoud be same such as (40.0 + 2.23)
print(int(2.23) + int(40))
print(float(2.23) + float(40))
# print(int(2.23))
# print(float(40))


#operater overloading
print("NO" + "Name")

#
print(x, y, z)
print(x+1, y*3, int((z/2) * 3))

#For remander
print(x % 2, y % 2)

#for power use(**)
print(y ** 100)

#find the mistake
Lalu = 1/3.0
print(Lalu)  