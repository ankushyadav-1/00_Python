distance = float(input("Enter your Distance in km(in numbers): "))
if distance <= 0.0:
    print("Enter Valid Distance.")
    exit()

if distance < 3.0:
    print("Cover your Distance by walking,Your distance is small.")
elif distance < 15.0:
    print("Cover your distance by Bike, Have a great ride.")
else:
    print("Cover your distance by Car,Your distance is too  large.")