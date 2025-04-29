n = int(input("Enter number for sum of even: "))
sum_even = 0

if n < 0:
    print("Enter positive number only.")
    exit()

for i in range(1 , n+1):
    if (i % 2 == 0):
        sum_even += i

print("Sum of even number: ", sum_even)