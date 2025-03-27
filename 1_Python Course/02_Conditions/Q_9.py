year = int(input("Enter your year(In number): "))

if year < 0:
    print("Enter Valid Year.")
    exit()

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is leap year.")
else:
    print(year, "is non-leap year.")