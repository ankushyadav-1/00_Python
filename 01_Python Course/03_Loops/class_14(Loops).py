#Q_1

numbers = [1, -2, 3 ,-4, 5, -6, 7, -8, 9, 0]
positive_number_count = 0

for num in numbers:
    if num > 0:
        positive_number_count += 1
print("Positive numbers:", positive_number_count)











#Q_2
n = int(input("Enter number for sum of even: "))
sum_even = 0

if n < 0:
    print("Enter positive number only.")
    exit()

for i in range(1 , n+1):
    if (i % 2 == 0):
        sum_even += i

print("Sum of even number: ", sum_even)







#Q_3
num_table = int(input("Enter your number for table: "))

if num_table < 0:
    print("Enter positive number only.")

for i in range(1 , 11):
    if i == 5:
        continue
    print(num_table, "x", i, "=", num_table * i)









#Q_4
input_str = input("Enter your string: ")
length = len(input_str)
r_str = ""

# for i in range(0, length):
#     r_str = r_str + input_str[length - 1 - i]

for i in range(length-1, -1, -1):
    r_str = r_str + input_str[i]

print(r_str)








# Q_5
in_str = input("Enter your string: ")

for char in in_str:
    if in_str.count(char) == 1:
        print("Char is: ", char)
        break



# Q_6
number = int(input("Enter your number: "))
factroial = 1
i = number

while i > 0:
    factroial = factroial * i
    i = i - 1

print("Factroial of number", number, "is",factroial) 










# Q_7
while True:
    num_from_user = int(input("Enter your number: "))

    if num_from_user >= 10 or num_from_user <= 1:
        print("You exit the program.")
        break



# Q_8
num = int(input("Enter your number: "))

is_prime = True

if num > 1:

    for i in range(2, num):
        if (num % i) == 0:
            is_prime = False
            break 
            
if is_prime == False:
    print(num, "is Composite number.")
else:
    print(num, "is a prime number.")




# Q_9
items = ["apple", "mango", "banana", "mango", "orange"]

unique_item = set()

for i in items:
    if i in unique_item:
        print("value repeted: ", i)
        break
    unique_item.add(i)