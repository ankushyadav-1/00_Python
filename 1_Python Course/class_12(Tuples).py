# tuple and list are similer, but we can change list.
tea_types = ("Black", "Green", "Oolong")
print(tea_types)
print(tea_types[0])
print(tea_types[-1])
print(tea_types[1:])
print(len(tea_types))

#we can't change Tuple
# print(tea_types[0]) = "Lemon"

# adding tuples
more_tea = ("Herbal", "Lemon", "Black")
all_tea = more_tea + tea_types
print(all_tea)
print(all_tea.count("Black"))
print(all_tea.count("Red"))

(black, green, Oolong) = tea_types
print(black)