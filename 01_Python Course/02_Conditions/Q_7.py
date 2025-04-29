print("Available coffee sizes \n 1.Small \n 2.Medium \n 3.Large")

order_size = input("Enter your coffee size(in words): ").lower()

if (order_size != "small") and (order_size != "medium") and (order_size != "large"):
    print("Enter only available sizes")
    exit()


extra_shot = (input("Do you want extra shot of espresso (Yes/No): ")).lower()

if (extra_shot != "yes") and (extra_shot != "no"):
    print("Enter Yes/No only for extra shot.")
    exit()

if extra_shot == "yes":
    order_is = (order_size + " size coffee with extra shot.")
else:
    order_is = order_size + " size coffee"

print(order_is)