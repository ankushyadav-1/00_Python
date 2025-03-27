def func(char,num):
    if num < 1 or num >= len(char):
        print("Enter valid number.")
        exit()

    print(char[num:])

func("ankush", 5)