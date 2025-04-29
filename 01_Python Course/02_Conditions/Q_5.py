print("Select wether conditions \n 1 for Sunny \n 2 for Rainy \n 3 for Snowy")
wether = int(input("Enter number of wether: "))

if wether > 3 or wether <= 0 :
    print("Invalid option.")
    exit()

if wether == 1:
    print("Go For a Walk.")
elif wether == 2:
    print("Read a Book.")
elif wether == 3:
    print("Bulid a Snowamn.")