# Q.1 :

Age = int(input("Give me your age: "))

if Age >= 0 and Age < 13:
    print("child")
elif Age >= 13 and Age < 20:
    print("Teenager")
elif Age >= 20 and Age < 60:
    print("Adult")
elif Age >= 60:
    print("Senior")
else: 
    print("It is not a valid age")





# Q.2 :
age = int(input("Enter your age: "))
day = str(input("Enter day: ")).lower()

# Amount = 0
# if age < 18:
#     Amount = 8
# else:
#     Amount = 12

Amount = 12 if age >= 18 else 8

if day == "wednesday":
    # Amount = Amount - 2
    Amount -= 2

print("Your movie ticket prize is: $", Amount)



# Q.3 
Marks = int(input("Enter your marks: "))
if Marks > 100:
    print("PLESE ENTER VALID MARKS.")
    exit()

if Marks >= 90:
    print("Your grade is 'A' ")
elif Marks >= 80:
    print("Your grade is 'B' ")
elif Marks >= 70:
    print("Your grade is 'C' ")
elif Marks >= 60:
    print("Your grade is 'D' ")
else:
    print("Your grade is 'F' ")




# Q.4 
print("Select your Banana colour: \n 1 for Green \n 2 for Yellow \n 3 for Brown")
colour = int(input("Enter your Banana color: "))

if colour > 3 or colour <= 0:
    print("Enter corect number.")
    exit()

if colour == 1:
    print("Your Banana is Unripe")
elif colour == 2:
    print("Your Banana is Ripe")
elif colour == 3:
    print("Your Banana is Overriped")






# Q.5
print("Select wether conditions \n 1 for Sunny \n 2 for Rainy \n 3 for Snowy")
wether = int(input("Enter number of wether: "))

if wether > 3 or wether <= 0 :
    print("Invalid option.")
    exit()

if wether == 1:
    print("Go For a Walk.")
elif wether == 2:
    print("Read a Book.")
elif wether == 3:
    print("Bulid a Snowamn.")






# Q_6
distance = float(input("Enter your Distance in km: "))
if distance < 0.1:
    print("Enter Valid Distance.")
    exit()

if distance < 3.0:
    print("Cover your Distance by walking.")
elif distance < 15.0:
    print("Cover your distance by Bike.")
else:
    print("Cover your distance by Car.")








# Q_7
print("Available coffee sizes \n 1.Small \n 2.Medium \n 3.Large")

order_size = input("Enter your coffee size: ").lower()

if (order_size != "small") and (order_size != "medium") and (order_size != "large"):
    print("Enter only available sizes")
    exit()


extra_shot = (input("Do you want extra shot of espresso (True/False): ")).lower()

if (extra_shot != "true") and (extra_shot != "false"):
    print("Enter True/False only for extra shot.")
    exit()

if extra_shot == "true":
    order_is = (order_size + " size coffee with extra shot.")
else:
    order_is = order_size + " size coffee"

print(order_is)








# Q_8
password = input("Enter your password: ")
length = len(password)

if length == 0:
    print("Please enetr your password.")
    exit()

if length < 6:
    print("Your password is weak.")
elif length <= 10:
    print("Your password is medium.")
else:
    print('Your password is strong.')




 

# Q_9
year = int(input("Enter your year: "))

if year < 0:
    print("Enter Valid Year.")
    exit()

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is leap year.")
else:
    print(year, "is non-leap year.")









# Q_10
print("Select your pet. \n 1.Dog \n 2.Cat")
pet = int(input("Enter Correct option according to your pet: "))

if pet < 1 or pet > 2:
    print("Enter correct option.")
    exit()

pet_age = int(input("Enter your pet age in years: "))
if pet_age < 0:
    print("Enter correct age.")
    exit()

if pet == 1:
    if pet_age < 2:
        print("Give Puppy food to your pet.")
    elif pet_age > 2:
        print("Don't give Puppy food to your pet.")

elif pet == 2:
    if pet_age > 5:
        print("Give senior Cat food to your pet.")
    elif pet_age < 5:
        print("Don't give senoir Cat food to your pet.")