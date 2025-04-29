print("Select your Banana colour: \n 1 for Green \n 2 for Yellow \n 3 for Brown")
colour = int(input("Enter your Banana color: "))

if colour > 3 or colour <= 0:
    print("Enter corect number.")
    exit()

if colour == 1:
    print("Your Banana is Unripe")
elif colour == 2:
    print("Your Banana is Ripe")
# elif colour == 3:
#     print("Your Banana is Overriped")
else:
    print("Your Banana is Overriped")