str_input = input("Enter your string: ")
numlen = len(str_input)

for i in range(0, numlen, 2):
    print(str_input[i])