import math

def circle(r):
    Area = math.pi * r ** 2
    circumference = 2 * math.pi * r
    return Area, circumference


input_user = int(input("Enter radius for Area and Circumference: ")) 
Area, circumference = circle(input_user)


print("Area of cirle: ", round(Area, 2), "\n", "circumference of circle: ", round(circumference, 2))