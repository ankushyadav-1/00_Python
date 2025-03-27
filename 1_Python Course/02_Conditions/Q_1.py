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