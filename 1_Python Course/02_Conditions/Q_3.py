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