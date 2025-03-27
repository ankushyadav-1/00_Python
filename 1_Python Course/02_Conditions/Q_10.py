print("Select your pet. \n 1.Dog \n 2.Cat")
pet = int(input("Enter Correct option according to your pet(In Number): "))

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