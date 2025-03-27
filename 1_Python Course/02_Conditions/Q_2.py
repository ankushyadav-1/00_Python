age = int(input("Enter your age: "))
day = str(input("Enter day(in words): ")).lower()


# Amount = 0
# if age < 18:
#     Amount = 8
# else:
#     Amount = 12

Amount = 8 if age <= 18 else 12


#days name to number
# monday = 1 
# tuesday = 2
# wednesday = 3
# thursday = 4
# friday = 5
# saturday = 6
# sunday = 7

if day == "wednesday" or day == "3":
    # Amount = Amount - 2
    Amount -= 2

print("Your movie ticket prize is: $", Amount)