#BASICS
name = "NoName"
# In terminal we directly print <name>
print(name)



#SLICE
Name = "Ankush Yadav"
first_char = Name[0]
print(first_char)

slice_Name = Name[0:7]
print(slice_Name)

# Name[0:7] in output first index included{0} but last index exclided{7}. 



#NUM_LIST
num_list = "0123456789"

print(num_list[:])

print(num_list[2:])

print(num_list[2:9])

print(num_list[0:10:2])

print(num_list[0:10:3])



#LOWER, UPPER
print(Name.lower())
print(Name.upper())
print(Name)



#STRIP, SPLIT
NAme = "         name     is non       "
print(NAme.strip())

NAME = "Ankush, Ram, Kalu, Lalu"
print(NAME.split())
print(NAME.split(", "))



# Replace
# print(Name)
print(Name.replace("Ankush", "ANkuSH"))
print(Name)


# Find
NAME = "ANKUSH YADAV"
print(NAME.find("A"))
# if it is present in orignal string, then it give Index of first reference,
# if it is not preesnt in orignal string, then it give Index(-1),
print(NAME.find("ankush"))

let = "ankush yadav"
print(let.count("a"))


chai_type = "masala"
Qty = 2
order = "I ordered {} cups of {} chai."
# print(order)
print(order.format(Qty, chai_type))



# list to str
chai_variety = ["Lemon", "masala", "ginger"]
# print("".join(chai_variety))
# print(" ".join(chai_variety))
print(", ".join(chai_variety))



# To find the length of str
# name = NoName
print(len(name))


# for print single letter in single line
for letter in name:
    print(letter)



# Reporting str used **(PATH PROBLEM)**
chai = "he said, \"masala cahi is good\""
print(chai)

    #**(PATH PROBLEM)**
namee = r"no\name" # r is RAW
print(namee)

# where (r) is usefull **(PATH PROBLEM)** **(bigest problem)
std = r"c:\\user\\name\\noname\\" #probelm
print(std)

std = r"c:\user\name\noname"
print(std)

#if we not useing r,
std = "c:\\user\\name\\noname"

# we can ask Qs form Python
name = "No Name"
print("No" in name)
print("no" in name)



# END OF STRING exclude [""" """](triple str)
