password = input("Enter your password: ")


#trime space
password = password.strip()
#trime left space
# password = password.lstrip()


length = len(password)

if length == 0:
    print("Password cannot be empty.")
    exit()


if length < 6:
    print("Your password is weak.")
elif length <= 10:
    print("Your password is medium.")
else:
    print('Your password is strong.')


# if " "== "  ":
#     print("true")
# else:
#     print("false")
