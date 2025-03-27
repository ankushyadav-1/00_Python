new_stars = int(input("Enter number: "))
if new_stars < 0:
    print("Enter +ve number.")
    exit()

for i in range(1, new_stars + 1):
    for p in range(1, new_stars + 1):
        print("*", end=" ")
    
    print("")