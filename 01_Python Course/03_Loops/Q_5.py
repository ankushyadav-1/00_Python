in_str = input("Enter your string: ")

for char in in_str:
    if in_str.count(char) == 1:
        print("Char is: ", char)
        break