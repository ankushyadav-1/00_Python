# Counting
counting = int(input("Enter number: "))
if counting < 0:
    print("Enter positive number only.")
    exit()


for i in range(1, counting + 1):
    print(i)