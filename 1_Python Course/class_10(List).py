tea_types = ["Black", "Green", "Oolong", "White"]
print(tea_types)

print(tea_types[0])
# print(tea_types[1])
# print(tea_types[:])
print(tea_types[:2])

tea_types[3] = "Herbal"
print(tea_types)

# Find the problem
# tea_types[1:2] = "Lemon"
# print(tea_types)

tea_types[1:2] = ["Lemon"]
print(tea_types)

tea_types[1:3] = ["White", "Green"]
print(tea_types)

print(tea_types[1:1])

tea_types[1:1] = ["tea"]
print(tea_types)

tea_types[1:2] = []
print(tea_types)

# Loops
for tea in tea_types:
    print(tea)

for tea in tea_types:
    print(tea, end="_")
    
print(" ")
tea_types.append("Oolong")

if "Oolong" in tea_types:
    print("I have Oolong tea")
    # if it have not given value it print nothing

# Remove last value fro list. We use pop method(function)
tea_types.pop()
print(tea_types)

# For Removing sepifice value from list. We use remove method(function)
tea_types.remove("Green")
print(tea_types)

#For adding some values in list. We use insert method
tea_types.insert(3, "green")
print(tea_types)

# For differ references in memory use cpoy method
tea_types_copy = tea_types.copy()
print(tea_types_copy)

#Just for fun
sq_num = [x**2 for x in range(11)]
print(sq_num)

cube_num = [y**3 for y in range(11)]
print(cube_num)