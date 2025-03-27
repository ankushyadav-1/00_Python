import math


# Q_1 Take a variable and Store float type values

x = 12.23

# (1.1) Convert it into int and print it.
print(int(x))  # output = 12

# (1.2) Floor and print.
print(math.floor(x))   # output = 12 

# (1.3) What wil be the output if we multiply with 10

# (1.3.1) without 10 converting into float
print(x * 10)    # output = 122.3

# (1.3.2) with 10 converting into float
print(x * float(10))     # output = 122.3





# Q_2 Take a string of fullname 

Name = "Himanshu Yadav"
Name_length = len(Name)

# (2.1) Print it's first, middle, last index
print(Name[0])                                      # output first index = H
print(Name[math.floor( (Name_length + 1) / 2 )])    # output middle index = u
print(Name[-1])                                     # output last index = v
print(Name[Name_length - 1])                        # output last index = v

# (2.2) slice first and last name and store in variable
First_name_old = Name[:6]
last_name_old = Name[6:]

print(First_name_old)      # output = Himanshu
print(last_name_old)       # output = Yadav

LengthOfName = len(Name)
space = Name.find(" ")
print("First Name is: ", Name[:space])
print("Last Name is: ", Name[space:])

# (2.3) Print first name in UPPER case and last name in lower case
print(First_name_old.upper())     # output = ANKUSH
print(last_name_old.lower())      # output = yadav





# Q_3 Take a umber string and slice into two half
num_srtING = ("987654321")

s = len(num_srtING)
mid = math.floor((s + 1) / 2)

first_half = num_srtING[ : mid]
second_half = num_srtING[mid : ]

print("first half is: ", first_half)                   # output = 98
print("second half is: ", second_half)                  # output = 76






# Q_4 Take a string with two names seprated by (,)  Print each name.

Names = "ankush,himanshu"
length = len(Names)
i = Names.find(",")

print("first name is: ", Names[ : i])        # output = ankush
print("Second name is: ", Names[ i+1 : ])        # output = himanshu





# Q_5 Give example of


# (5.1) Replace method
print(Names.replace("ankush", "a"))
print(Names)

# (5.2) Find method
print(Names.find("h"))

# (5.3) Count method
print(Names.count("a"))

# (5.4) format method
my_name = "Ankush"
bro_name = "Himanshu"
sentence = "My name is {} and My brother name is {}."
print(sentence.format(my_name, bro_name))

# (5.5) Join method
NAMES_list = ["Ankush", "Himanshu"]
print("_".join(NAMES_list))