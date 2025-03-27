input_str = input("Enter your string: ")
r_str = ""


# length = len(input_str)

# for i in range(0, length):
#     r_str = r_str + input_str[length - 1 - i]

# for i in range(length-1, -1, -1):
#     r_str = r_str + input_str[i]


for c in input_str:
    r_str = c + r_str 

print(r_str)