#print stars
user_input = int(input("Enter number for print stars: "))
if user_input < 0:
    print("Enter postive Value.")
    exit()

for i in range(1, user_input + 1):
    print("*", end =" ")
