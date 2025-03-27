# Given two integer numbers, return their product only if
# the product is equal to or lower than 1000. Otherwise, return their sum.

def func():

    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))

    if (num1 * num2) <= 1000:
        # print("Product of two numbers is = ", num1 * num2)
        return num1 * num2

    else:
        # print("Sum of two numbers is = ", num1 + num2)
        return num1 + num2

ans = func()
print("ans is = ", ans)

ans = func()
print("ans is = ", ans)