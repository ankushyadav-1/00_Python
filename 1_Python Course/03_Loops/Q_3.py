num_table = int(input("Enter your number for table: "))

if num_table < 0:
    print("Enter positive number only.")

for i in range(1 , 11):
    if i == 5:
        continue
    print(num_table, "x", i, "=", num_table * i)