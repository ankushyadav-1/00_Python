user = {"0": "No Name", "1": "Ankush", "2": "ankush"}
print(user)
print(user["1"])

user["1"] = "Ankush Yadav"
print(user)
print(user["1"])
print(user.get("2"))

#Loop in Dictinary

# For print keys only
for Name in user:
    print(Name)

    
#For print keys and valuses. 
for Name in user:
    print(Name, user[Name])

for key, value in user.items():
    print(key, value)


#Conditions
if "0" in user:
    print("I have masala chai")


#Find the items in Dictionary
print(len(user))


#For adding new items
user["3"] = "Himanshu"
print(user)

#For removing items from our choice.
user.pop("2")
print(user)

#Pop recent items
user.popitem()
print(user)

#For delete items from memory
del user["1"]
print(user)

#For copy the dictionary
user_copy = user.copy()
print(user_copy)


#Let open a tea_shop
tea_shop = {
    "chai": {"masala": "spicy", "Ginger": "Zesty"},
    "Tea" : {"Green": "Mild", "Black": "Strong"}
}

print(tea_shop)
print()
print(tea_shop["chai"]["Ginger"])

#sq_num in Dictionary
sq_num = {x:x**2 for x in range(6)}
print(sq_num)

#for clear items.
print(sq_num.clear())

# make dect by using list and single deftault values.
list = ["Ginger", "Lemon", "Masala"]
deftault_values = "Good"
my_dict = dict.fromkeys(list, deftault_values)
print(my_dict)

# make dect by using list and many deftault values.
my_dict = dict.fromkeys(list, list)
print(my_dict)